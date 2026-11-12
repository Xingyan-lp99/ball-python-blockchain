"""Registration workflow; profile data and contract rules remain separate."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from blockchain.transactions import (
    CHAIN_ERRORS, TransactionProblem as RegistrationProblem,
    transaction_lock as registration_lock, persist_receipt,
    transaction_report,
)
from snake_registry.local_chain import ChainConflict, ChainStale
from snake_registry.models import RegistrationAttempt, Snake
from snake_registry.schemas import RegistrationRead


def latest_attempt(session: Session, snake: Snake) -> RegistrationAttempt | None:
    return session.scalar(
        select(RegistrationAttempt).where(RegistrationAttempt.snake_id == snake.id)
        .order_by(RegistrationAttempt.created_at.desc(), RegistrationAttempt.id.desc()).limit(1)
    )


def report(attempt: RegistrationAttempt | None, check: str = "not_checked", error: str | None = None) -> RegistrationRead:
    return transaction_report(attempt, check, error)


def save_receipt(session: Session, snake: Snake, attempt: RegistrationAttempt, chain) -> RegistrationRead:
    if not persist_receipt(session, snake.snake_id, attempt, chain):
        return report(attempt, "verified", "Awaiting a transaction receipt; not confirmed")
    return report(attempt, "verified", attempt.failure_code)


def reconcile(session: Session, snake: Snake, attempt: RegistrationAttempt | None, chain) -> RegistrationRead:
    chain.validate_scope()
    if attempt and (
        attempt.chain_id != chain.chain_id
        or attempt.contract_address.lower() != chain.address.lower()
        or attempt.instance_id != chain.instance_id
        or attempt.manager_address.lower() != chain.manager.lower()
    ):
        raise ChainStale
    manager = chain.manager_of(snake.snake_id)
    if manager and manager.lower() != chain.manager.lower():
        raise ChainConflict
    if manager:
        transaction_hash = chain.registration_hash(snake.snake_id)
        if not transaction_hash:
            raise ChainConflict
        if attempt is None:
            attempt = RegistrationAttempt(
                snake_id=snake.id, chain_id=chain.chain_id, contract_address=chain.address,
                instance_id=chain.instance_id, manager_address=chain.manager,
                start_block=0, status="submitted", transaction_hash=transaction_hash,
            )
            session.add(attempt)
            session.commit()
        elif attempt.transaction_hash != transaction_hash:
            # Keep a previous failed attempt rather than rewriting its evidence.
            if attempt.status == "failed":
                recovered = RegistrationAttempt(
                    snake_id=snake.id, chain_id=chain.chain_id, contract_address=chain.address,
                    instance_id=chain.instance_id, manager_address=chain.manager,
                    start_block=0, status="submitted", transaction_hash=transaction_hash,
                )
                session.add(recovered)
                attempt = recovered
            else:
                attempt.transaction_hash = transaction_hash
                attempt.status = "submitted"
            session.commit()
        return save_receipt(session, snake, attempt, chain)
    if attempt:
        if attempt.status == "confirmed":
            raise ChainStale
        if not attempt.transaction_hash and attempt.nonce is not None:
            transaction_hash = chain.recover_hash(attempt.nonce, attempt.start_block, snake.snake_id)
            if transaction_hash:
                attempt.transaction_hash = transaction_hash
                attempt.status = "submitted"
                session.commit()
        if attempt.transaction_hash:
            return save_receipt(session, snake, attempt, chain)
    return report(attempt, "verified", attempt.failure_code if attempt else None)


def registration_state(session: Session, snake: Snake, chain_factory) -> RegistrationRead:
    attempt = latest_attempt(session, snake)
    # No chain configuration is needed for a database-only profile.
    if attempt is None:
        return report(None)
    try:
        with registration_lock(session):
            return reconcile(session, snake, attempt, chain_factory())
    except ChainStale:
        return report(attempt, "stale", "Local deployment changed or chain reset; historical evidence is not current")
    except ChainConflict:
        return report(attempt, "conflict", "On-chain identity or transaction conflicts with the expected registration")
    except CHAIN_ERRORS:
        return report(attempt, "unavailable", "Local chain unavailable; confirmation cannot be established")
    except RegistrationProblem:
        return report(attempt, "not_checked", "Another registration is processing; refresh shortly")


def submit_registration(session: Session, snake: Snake, breeder_id: str, chain_factory) -> RegistrationRead:
    if breeder_id != "BR001" or snake.current_manager_id != breeder_id or snake.breeder_id != breeder_id:
        raise RegistrationProblem(403, "Only the current demo manager may register this profile")
    with registration_lock(session):
        attempt = latest_attempt(session, snake)
        try:
            chain = chain_factory()
            state = reconcile(session, snake, attempt, chain)
            attempt = latest_attempt(session, snake)
            if state.status == "confirmed":
                return state
            if attempt and attempt.transaction_hash and attempt.status != "failed":
                return state
            if attempt is None or attempt.status == "failed":
                nonce, gas_price, start_block = chain.transaction_parameters()
                reserved = session.scalar(
                    select(RegistrationAttempt).where(
                        RegistrationAttempt.chain_id == chain.chain_id,
                        RegistrationAttempt.instance_id == chain.instance_id,
                        RegistrationAttempt.manager_address == chain.manager,
                        RegistrationAttempt.nonce == nonce,
                        RegistrationAttempt.status.in_(["prepared", "submitted"]),
                    ).limit(1)
                )
                if reserved:
                    raise RegistrationProblem(409, "A previous registration reserves this wallet nonce; refresh its status first")
                attempt = RegistrationAttempt(
                    snake_id=snake.id, chain_id=chain.chain_id, contract_address=chain.address,
                    instance_id=chain.instance_id, manager_address=chain.manager,
                    nonce=nonce, gas_price=gas_price, start_block=start_block,
                )
                session.add(attempt)
                # If this fails, nothing has been broadcast.
                session.commit()
            transaction_hash = chain.send(snake.snake_id, attempt.nonce, attempt.gas_price)
            attempt.transaction_hash = transaction_hash
            attempt.status = "submitted"
            # Persist the hash immediately, before receipt polling/verification.
            session.commit()
            return save_receipt(session, snake, attempt, chain)
        except ChainStale:
            raise RegistrationProblem(409, "Local deployment changed or chain reset; historical evidence retained") from None
        except ChainConflict:
            raise RegistrationProblem(409, "On-chain registration conflicts with the expected identity or transaction") from None
        except CHAIN_ERRORS:
            if attempt:
                # An uncertain broadcast is still processing. Never infer failure.
                return report(attempt, "unavailable", "Local chain response unavailable; refresh before retrying")
            raise RegistrationProblem(503, "Local chain deployment/RPC unavailable; registration not submitted") from None
