import hashlib
import json
import getpass
from pathlib import Path

import psycopg
from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import ContractCustomError, TimeExhausted, Web3Exception

from backend.deploy_registry import ARTIFACT_PATH, SNAKE_NOT_FOUND
from backend.photos import save_snake_photo


ROOT = Path(__file__).resolve().parents[1]
SEPOLIA_ENV_PATH = ROOT / ".env.sepolia"
SEPOLIA_STATE_PATH = ROOT / "storage/sepolia/sepolia-p0-001/state.json"
EXPECTED_CHAIN_ID = 11155111
EXPECTED_SELLER = Web3.to_checksum_address(
    "0x53c31f84Ea3F2b0A1c856a30ab519b8c8Dc55a57"
)
MAX_FEE_PER_GAS = Web3.to_wei(1, "gwei")
REGISTER_GAS_CAP = 200_000
_SEPOLIA_SIGNERS: dict[str, object] = {}


class SepoliaRegistrationError(RuntimeError):
    def __init__(self, message: str, *, outcome: str, transaction_hash: str | None = None):
        super().__init__(message)
        self.outcome = outcome
        self.transaction_hash = transaction_hash


def configure_seller_signer(private_key: str) -> None:
    configure_sepolia_signer("BREEDER001", private_key, EXPECTED_SELLER)


def configure_sepolia_signer(
    participant_id: str, private_key: str, expected_address: str
) -> None:
    try:
        account = Web3().eth.account.from_key(private_key.strip())
    except (TypeError, ValueError):
        raise SepoliaRegistrationError("A local Sepolia key is invalid.", outcome="not_submitted") from None
    if account.address != Web3.to_checksum_address(expected_address):
        raise SepoliaRegistrationError(
            f"The entered key does not match {participant_id}'s configured Sepolia address.",
            outcome="not_submitted",
        )
    _SEPOLIA_SIGNERS[participant_id] = account


def get_sepolia_signer(participant_id: str):
    signer = _SEPOLIA_SIGNERS.get(participant_id)
    if signer is None:
        raise SepoliaRegistrationError(
            f"The local signing session is missing {participant_id}; no transaction was sent.",
            outcome="not_submitted",
        )
    return signer


def configure_local_sepolia_signers() -> None:
    values = _read_env_file()
    _, _, state = _registry_artifacts()
    buyer_address = values.get("SEPOLIA_BUYER_ADDRESS", "")
    if not Web3.is_address(buyer_address):
        raise SepoliaRegistrationError(
            "Add the public SEPOLIA_BUYER_ADDRESS to .env.sepolia before starting the Sepolia demo.",
            outcome="not_submitted",
        )
    identities = {
        "BREEDER001": ("Seller", state["identity"]["seller"]),
        "BUYER001": ("Buyer", buyer_address),
        "LAB001": ("LAB001", state["identity"]["laboratories"][0]),
        "LAB002": ("LAB002", state["identity"]["laboratories"][1]),
    }
    for participant_id, (label, address) in identities.items():
        private_key = getpass.getpass(f"{label} Sepolia private key (hidden, memory only): ")
        configure_sepolia_signer(participant_id, private_key, address)
        private_key = ""


def _read_env_file() -> dict[str, str]:
    if not SEPOLIA_ENV_PATH.is_file():
        raise SepoliaRegistrationError("Local Sepolia configuration is unavailable.", outcome="not_submitted")
    values: dict[str, str] = {}
    for line in SEPOLIA_ENV_PATH.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        key = key.strip()
        if not separator or key in values:
            raise SepoliaRegistrationError("Local Sepolia configuration is invalid.", outcome="not_submitted")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    if not values.get("SEPOLIA_RPC_URL", "").startswith("https://"):
        raise SepoliaRegistrationError("A local HTTPS Sepolia RPC URL is required.", outcome="not_submitted")
    return values


def _registry_artifacts() -> tuple[str, dict, dict]:
    try:
        state = json.loads(SEPOLIA_STATE_PATH.read_text(encoding="utf-8"))
        artifact_bytes = ARTIFACT_PATH.read_bytes()
        artifact = json.loads(artifact_bytes)
        expected_hash = state["identity"]["artifacts"]["SnakeRegistry"]
        registry_address = state["steps"][0]["evidence"]["contract_address"]
        if (
            state["identity"]["chain_id"] != EXPECTED_CHAIN_ID
            or state["identity"]["seller"] != EXPECTED_SELLER
            or state["steps"][0]["name"] != "SnakeRegistry"
            or state["steps"][0]["status"] != "confirmed"
            or hashlib.sha256(artifact_bytes).hexdigest() != expected_hash
        ):
            raise ValueError
    except (OSError, ValueError, KeyError, TypeError, IndexError):
        raise SepoliaRegistrationError(
            "The saved Sepolia deployment checkpoint or Artifact does not match.",
            outcome="not_submitted",
        ) from None
    return registry_address, artifact, state


def register_pet_on_sepolia(
    connection: psycopg.Connection,
    *,
    participant_id: str,
    profile: dict[str, object],
    photo_content: bytes,
) -> dict[str, str | int]:
    if participant_id != "BREEDER001":
        raise SepoliaRegistrationError("Only the configured Seller may register pets on Sepolia.", outcome="not_submitted")
    account = get_sepolia_signer(participant_id)

    values = _read_env_file()
    registry_address, artifact, _ = _registry_artifacts()
    try:
        client = Web3(Web3.HTTPProvider(
            values["SEPOLIA_RPC_URL"],
            request_kwargs={"timeout": 20},
            exception_retry_configuration=None,
        ))
        if not client.is_connected() or client.eth.chain_id != EXPECTED_CHAIN_ID:
            raise SepoliaRegistrationError("Sepolia RPC or Chain ID verification failed.", outcome="not_submitted")
        registry_address = Web3.to_checksum_address(registry_address)
        if not client.eth.get_code(registry_address):
            raise SepoliaRegistrationError("Saved SnakeRegistry has no deployed code.", outcome="not_submitted")
        if account.address != EXPECTED_SELLER:
            raise SepoliaRegistrationError("Configured Seller key does not match the approved Sepolia address.", outcome="not_submitted")
        registry = client.eth.contract(address=registry_address, abi=artifact["abi"])
    except SepoliaRegistrationError:
        raise
    except (RequestException, Web3Exception, OSError, ValueError, KeyError):
        raise SepoliaRegistrationError("Sepolia preflight failed; no transaction was sent.", outcome="not_submitted") from None

    pet_id = str(profile["snake_id"])
    try:
        with connection.transaction():
            participant = connection.execute(
                "SELECT 1 FROM public.participants WHERE participant_id = %s",
                (participant_id,),
            ).fetchone()
            if participant is None:
                raise SepoliaRegistrationError("The Seller participant is not configured in the database.", outcome="not_submitted")
            existing = connection.execute(
                "SELECT transaction_hash FROM public.sepolia_pet_registrations WHERE snake_id = %s",
                (pet_id,),
            ).fetchone()
            if existing is not None:
                raise SepoliaRegistrationError(
                    "This Pet ID has a saved Sepolia transaction checkpoint. Check its Hash; it will not be resubmitted.",
                    outcome="unknown",
                    transaction_hash=existing[0],
                )
        try:
            registry.functions.getCurrentKeeper(pet_id).call()
        except ContractCustomError as error:
            if error.data != SNAKE_NOT_FOUND:
                raise SepoliaRegistrationError("On-chain Pet ID lookup failed.", outcome="not_submitted") from None
        else:
            raise SepoliaRegistrationError("This Pet ID is already registered on Sepolia.", outcome="not_submitted")

        latest_nonce = client.eth.get_transaction_count(account.address, "latest")
        pending_nonce = client.eth.get_transaction_count(account.address, "pending")
        if latest_nonce != pending_nonce:
            raise SepoliaRegistrationError("Seller has a pending transaction; inspect it before continuing.", outcome="not_submitted")
        block = client.eth.get_block("latest")
        priority_fee = client.eth.max_priority_fee
        max_fee = 2 * block["baseFeePerGas"] + priority_fee
        if not 0 < max_fee <= MAX_FEE_PER_GAS:
            raise SepoliaRegistrationError("Current Sepolia fee exceeds the 1 Gwei limit.", outcome="not_submitted")
        contract_call = registry.functions.registerSnake(pet_id)
        tx = contract_call.build_transaction({
            "from": account.address,
            "chainId": EXPECTED_CHAIN_ID,
            "nonce": latest_nonce,
            "value": 0,
            "maxFeePerGas": max_fee,
            "maxPriorityFeePerGas": priority_fee,
        })
        estimated_gas = client.eth.estimate_gas(tx)
        gas_limit = (estimated_gas * 120 + 99) // 100
        if gas_limit > REGISTER_GAS_CAP:
            raise SepoliaRegistrationError(
                f"Estimated registration Gas ({gas_limit}) exceeds the {REGISTER_GAS_CAP} limit.",
                outcome="not_submitted",
            )
        tx["gas"] = gas_limit
        if client.eth.get_balance(account.address) < gas_limit * max_fee:
            raise SepoliaRegistrationError("Seller balance is below the estimated maximum transaction cost.", outcome="not_submitted")

        photo_reference = save_snake_photo(photo_content)
        signed = account.sign_transaction(tx)
        transaction_hash = signed.hash.to_0x_hex()
        with connection.transaction():
            connection.execute(
                """
                INSERT INTO public.sepolia_pet_registrations (
                    snake_id, participant_id, species, sex, date_of_birth,
                    genetic_description, nickname, introduction,
                    sire_description, dam_description, photo_reference,
                    contract_address, transaction_hash, transaction_nonce,
                    transaction_status
                ) VALUES (
                    %(snake_id)s, %(participant_id)s, %(species)s, %(sex)s,
                    %(date_of_birth)s, %(genetic_description)s, %(nickname)s,
                    %(introduction)s, %(sire_description)s, %(dam_description)s,
                    %(photo_reference)s, %(contract_address)s,
                    %(transaction_hash)s, %(transaction_nonce)s, 'prepared'
                )
                """,
                {
                    **profile,
                    "participant_id": participant_id,
                    "photo_reference": photo_reference,
                    "contract_address": registry_address,
                    "transaction_hash": transaction_hash,
                    "transaction_nonce": latest_nonce,
                },
            )
    except SepoliaRegistrationError:
        raise
    except psycopg.errors.UniqueViolation:
        raise SepoliaRegistrationError("This Pet ID or transaction already has a Sepolia checkpoint; no transaction was sent.", outcome="not_submitted") from None
    except (psycopg.Error, RequestException, Web3Exception, ValueError, OSError):
        raise SepoliaRegistrationError("Sepolia registration preflight failed; no transaction was sent.", outcome="not_submitted") from None

    try:
        if client.eth.chain_id != EXPECTED_CHAIN_ID or client.eth.get_transaction_count(account.address, "pending") != latest_nonce:
            raise SepoliaRegistrationError("Chain or nonce changed after checkpointing.", outcome="unknown", transaction_hash=transaction_hash)
        if client.eth.get_balance(account.address) < gas_limit * max_fee:
            raise SepoliaRegistrationError("Seller balance changed before broadcast.", outcome="unknown", transaction_hash=transaction_hash)
        returned_hash = client.eth.send_raw_transaction(signed.raw_transaction).to_0x_hex()
        if returned_hash.lower() != transaction_hash.lower():
            raise SepoliaRegistrationError("RPC returned a different transaction hash.", outcome="unknown", transaction_hash=transaction_hash)
        with connection.transaction():
            connection.execute(
                "UPDATE public.sepolia_pet_registrations SET transaction_status = 'submitted', updated_at = CURRENT_TIMESTAMP WHERE transaction_hash = %s",
                (transaction_hash,),
            )
        receipt = client.eth.wait_for_transaction_receipt(transaction_hash, timeout=120)
        if receipt["status"] != 1:
            with connection.transaction():
                connection.execute(
                    "UPDATE public.sepolia_pet_registrations SET transaction_status = 'failed', receipt_status = 0, updated_at = CURRENT_TIMESTAMP WHERE transaction_hash = %s",
                    (transaction_hash,),
                )
            raise SepoliaRegistrationError("Sepolia registration Receipt failed.", outcome="failed", transaction_hash=transaction_hash)
        events = registry.events.SnakeRegistered().process_receipt(receipt)
        if len(events) != 1:
            raise SepoliaRegistrationError("Receipt succeeded, but SnakeRegistered verification failed.", outcome="unverified", transaction_hash=transaction_hash)
        event = events[0]
        if event["address"] != registry_address or event["args"]["snakeId"] != pet_id or event["args"]["keeper"] != account.address:
            raise SepoliaRegistrationError("Receipt event did not match the submitted Pet ID and Seller.", outcome="unverified", transaction_hash=transaction_hash)
        if registry.functions.getCurrentKeeper(pet_id).call() != account.address:
            raise SepoliaRegistrationError("On-chain Initial Keeper verification failed.", outcome="unverified", transaction_hash=transaction_hash)
        try:
            with connection.transaction():
                connection.execute(
                    """
                    UPDATE public.sepolia_pet_registrations
                    SET transaction_status = 'confirmed', receipt_status = 1,
                        initial_keeper = %s, current_keeper = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE transaction_hash = %s
                    """,
                    (account.address, account.address, transaction_hash),
                )
        except psycopg.Error:
            raise SepoliaRegistrationError("Chain registration succeeded, but Sepolia database sync failed. Check this Hash before retrying.", outcome="storage_error", transaction_hash=transaction_hash) from None
        return {
            "transaction_hash": transaction_hash,
            "receipt_status": 1,
            "snake_id": pet_id,
            "initial_keeper": account.address,
            "contract_address": registry_address,
            "etherscan_url": f"https://sepolia.etherscan.io/tx/{transaction_hash}",
            "chain_id": EXPECTED_CHAIN_ID,
            "estimated_gas": estimated_gas,
            "gas_limit": gas_limit,
            "max_fee_per_gas": max_fee,
            "max_cost_wei": gas_limit * max_fee,
        }
    except SepoliaRegistrationError:
        raise
    except (RequestException, Web3Exception, TimeExhausted, psycopg.Error, ValueError):
        try:
            with connection.transaction():
                connection.execute(
                    "UPDATE public.sepolia_pet_registrations SET transaction_status = 'unknown', updated_at = CURRENT_TIMESTAMP WHERE transaction_hash = %s AND transaction_status <> 'confirmed'",
                    (transaction_hash,),
                )
        except psycopg.Error:
            pass
        raise SepoliaRegistrationError(
            "Transaction outcome is unknown. Use the saved Hash to check it; do not resubmit.",
            outcome="unknown",
            transaction_hash=transaction_hash,
        ) from None
