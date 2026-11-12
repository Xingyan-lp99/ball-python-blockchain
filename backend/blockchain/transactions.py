from contextlib import contextmanager

from requests.exceptions import RequestException
from sqlalchemy import text
from web3.exceptions import Web3Exception

from snake_registry.local_chain import ChainStale, ChainUnavailable, hex_value
from snake_registry.schemas import RegistrationRead

CHAIN_ERRORS = (ChainUnavailable, RequestException, Web3Exception, OSError, ValueError, KeyError)


class TransactionProblem(Exception):
    def __init__(self, status_code: int, detail: str, code: str | None = None):
        self.status_code = status_code
        self.detail = detail
        self.code = code


@contextmanager
def transaction_lock(session):
    # Same lock as the existing registration workflow, held across commits.
    with session.get_bind().connect() as connection:
        acquired = connection.scalar(text("SELECT pg_try_advisory_lock(724801002)"))
        if not acquired:
            raise TransactionProblem(409, "Another transaction is processing; refresh and retry")
        try:
            yield
        finally:
            connection.execute(text("SELECT pg_advisory_unlock(724801002)"))


def transaction_report(attempt, check="not_checked", error=None) -> RegistrationRead:
    status = "not_submitted"
    if attempt:
        status = {"prepared": "processing", "submitted": "processing"}.get(attempt.status, attempt.status)
        if check in {"stale", "conflict"}:
            status = "failed"
        elif status == "confirmed" and check != "verified":
            status = "processing"
    fields = ["transaction_hash", "chain_id", "contract_address", "manager_address", "block_number", "block_hash", "instance_id"]
    return RegistrationRead(
        status=status, chain_check=check, error=error,
        recorded_status=attempt.status if attempt else None,
        **{field: getattr(attempt, field) if attempt else None for field in fields},
    )


def persist_receipt(session, subject, attempt, chain) -> bool:
    receipt = chain.receipt(attempt.transaction_hash)
    if receipt is None:
        if attempt.status == "confirmed":
            raise ChainStale
        return False
    if receipt["status"] != 1:
        attempt.status = "failed"
        attempt.failure_code = "transaction_reverted"
    else:
        chain.verify_success(subject, attempt.transaction_hash, receipt)
        attempt.status = "confirmed"
        attempt.failure_code = None
    attempt.block_number = receipt["blockNumber"]
    attempt.block_hash = hex_value(receipt["blockHash"])
    session.commit()
    return True
