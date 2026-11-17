import json
from collections.abc import Callable
from datetime import datetime, timezone

from web3 import Web3
from web3.contract import Contract
from web3.contract.contract import ContractFunction
from web3.exceptions import ContractLogicError
from web3.types import TxReceipt

from backend.blockchain import get_current_keeper
from backend.setup_certificates import CERTIFICATE_ARTIFACT_PATH


class CertificateTransactionError(RuntimeError):
    """Preserve transaction identity when issuance cannot report success."""

    def __init__(
        self,
        message: str,
        *,
        transaction_hash: str | None,
        outcome: str,
    ) -> None:
        super().__init__(message)
        self.transaction_hash = transaction_hash
        self.outcome = outcome


# Purpose: connect reads and writes to the intended local certificate contract.
# Without this check, history could be read from a different registry or chain.
def connect_certificate_registry(
    *,
    certificate_address: str,
    snake_registry_address: str,
) -> tuple[Web3, Contract]:
    client = Web3(
        Web3.HTTPProvider(
            "http://127.0.0.1:8545",
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )

    if not client.is_connected():
        raise ConnectionError("Cannot connect to the blockchain node.")

    if client.eth.chain_id != 31337:
        raise ConnectionError("Unexpected blockchain chain ID.")

    address = Web3.to_checksum_address(certificate_address)

    if not client.eth.get_code(address):
        raise ConnectionError("Certificate contract code is unavailable.")

    artifact = json.loads(
        CERTIFICATE_ARTIFACT_PATH.read_text(encoding="utf-8")
    )
    registry = client.eth.contract(
        address=address,
        abi=artifact["abi"],
    )

    linked_registry = registry.functions.snakeRegistry().call()

    if linked_registry.lower() != snake_registry_address.lower():
        raise ConnectionError(
            "The certificate contract references a different snake registry."
        )

    return client, registry


# Purpose: check laboratory permission and snake existence before a write.
# Without these checks, obvious permission failures would leave local drafts.
def prepare_certificate_issuance(
    *,
    certificate_address: str,
    snake_registry_address: str,
    sender_address: str,
    snake_id: str,
) -> tuple[Web3, Contract]:
    client, registry = connect_certificate_registry(
        certificate_address=certificate_address,
        snake_registry_address=snake_registry_address,
    )
    sender = Web3.to_checksum_address(sender_address)

    if not registry.functions.isAuthorizedLaboratory(sender).call():
        raise PermissionError(
            "This laboratory is not authorized to issue certificates."
        )

    get_current_keeper(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
        contract_address=snake_registry_address,
        snake_id=snake_id,
    )

    return client, registry


# Purpose: retain submission and confirmation handling for both certificate writes.
# Without this helper, issuance and revision could handle unknown results differently.
def _submit_certificate_transaction(
    *,
    client: Web3,
    function: ContractFunction,
    sender_address: str,
    on_submitted: Callable[[str], None],
) -> TxReceipt:
    sender = Web3.to_checksum_address(sender_address)

    try:
        transaction_hash = function.transact({"from": sender})
    except ContractLogicError:
        raise CertificateTransactionError(
            "The contract rejected the request. No transaction was submitted.",
            transaction_hash=None,
            outcome="not_submitted",
        ) from None
    except Exception:
        # A lost RPC response may hide a transaction accepted by the node.
        raise CertificateTransactionError(
            "Submission could not be confirmed. "
            "Check the chain before submitting again.",
            transaction_hash=None,
            outcome="unknown",
        ) from None

    transaction_hex = transaction_hash.to_0x_hex()

    try:
        on_submitted(transaction_hex)
    except Exception:
        raise CertificateTransactionError(
            "The transaction was submitted, but its hash could not be saved.",
            transaction_hash=transaction_hex,
            outcome="storage_error",
        ) from None

    try:
        receipt = client.eth.wait_for_transaction_receipt(
            transaction_hash,
            timeout=30,
        )
    except Exception:
        raise CertificateTransactionError(
            "The transaction is awaiting confirmation. "
            "Check it before submitting again.",
            transaction_hash=transaction_hex,
            outcome="unknown",
        ) from None

    if receipt["status"] != 1:
        raise CertificateTransactionError(
            "The certificate transaction failed.",
            transaction_hash=transaction_hex,
            outcome="failed",
        )

    return receipt


# Purpose: submit V1 and verify its receipt, event, and stored evidence.
# Without confirmation, a submitted transaction could be shown as a
# successfully issued certificate even when its result is unknown.
def issue_certificate_on_chain(
    *,
    client: Web3,
    registry: Contract,
    sender_address: str,
    snake_id: str,
    series_id: str,
    version_id: str,
    file_hash: str,
    on_submitted: Callable[[str], None],
) -> dict:
    sender = Web3.to_checksum_address(sender_address)
    digest = bytes.fromhex(file_hash)
    receipt = _submit_certificate_transaction(
        client=client,
        function=registry.functions.issueCertificate(
            snake_id, series_id, version_id, digest
        ),
        sender_address=sender,
        on_submitted=on_submitted,
    )
    transaction_hex = receipt["transactionHash"].to_0x_hex()

    try:
        signature = Web3.keccak(
            text="CertificateIssued(string,string,string,address,uint256,bytes32)"
        )

        matching_logs = [
            log
            for log in receipt["logs"]
            if log["address"].lower() == registry.address.lower()
            and len(log["topics"]) == 4
            and bytes(log["topics"][0]) == bytes(signature)
        ]

        if len(matching_logs) != 1:
            raise ValueError("Expected one certificate issuance event.")

        event = registry.events.CertificateIssued().process_log(
            matching_logs[0]
        )
        arguments = event["args"]

        if not (
            bytes(arguments["seriesId"])
            == bytes(Web3.keccak(text=series_id))
            and bytes(arguments["versionId"])
            == bytes(Web3.keccak(text=version_id))
            and arguments["snakeId"] == snake_id
            and arguments["issuer"].lower() == sender.lower()
            and arguments["versionNumber"] == 1
            and bytes(arguments["fileHash"]) == digest
        ):
            raise ValueError("The issuance event does not match the request.")

        evidence = registry.functions.getVersion(version_id).call(
            block_identifier=receipt["blockNumber"]
        )

        if not (
            list(evidence[:5])
            == [snake_id, series_id, version_id, 1, ""]
            and evidence[5].lower() == sender.lower()
            and bytes(evidence[6]) == digest
            and evidence[7] == 1
        ):
            raise ValueError("The stored version does not match the request.")

        block = client.eth.get_block(receipt["blockNumber"])
        issued_at = datetime.fromtimestamp(
            block["timestamp"],
            tz=timezone.utc,
        )
    except Exception:
        raise CertificateTransactionError(
            "The transaction succeeded, but its certificate evidence "
            "could not be verified. Do not submit again automatically.",
            transaction_hash=transaction_hex,
            outcome="unverified",
        ) from None

    return {
        "transaction_hash": transaction_hex,
        "receipt_status": 1,
        "issued_at": issued_at,
    }


# Purpose: append a revision and verify both the new and superseded versions.
# Without this check, the backend could label the wrong predecessor as superseded.
def revise_certificate_on_chain(
    *,
    client: Web3,
    registry: Contract,
    sender_address: str,
    snake_id: str,
    series_id: str,
    version_id: str,
    version_number: int,
    previous_version_id: str,
    file_hash: str,
    on_submitted: Callable[[str], None],
) -> dict:
    sender = Web3.to_checksum_address(sender_address)
    digest = bytes.fromhex(file_hash)
    receipt = _submit_certificate_transaction(
        client=client,
        function=registry.functions.appendRevision(
            series_id, version_id, digest
        ),
        sender_address=sender,
        on_submitted=on_submitted,
    )
    transaction_hex = receipt["transactionHash"].to_0x_hex()

    try:
        signature = Web3.keccak(
            text="CertificateRevised(string,string,string,address,uint256,bytes32)"
        )
        matching_logs = [
            log
            for log in receipt["logs"]
            if log["address"].lower() == registry.address.lower()
            and len(log["topics"]) == 4
            and bytes(log["topics"][0]) == bytes(signature)
        ]

        if len(matching_logs) != 1:
            raise ValueError("Expected one certificate revision event.")

        arguments = registry.events.CertificateRevised().process_log(
            matching_logs[0]
        )["args"]

        if not (
            bytes(arguments["seriesId"]) == bytes(Web3.keccak(text=series_id))
            and bytes(arguments["previousVersionId"])
            == bytes(Web3.keccak(text=previous_version_id))
            and bytes(arguments["versionId"])
            == bytes(Web3.keccak(text=version_id))
            and arguments["issuer"].lower() == sender.lower()
            and arguments["versionNumber"] == version_number
            and bytes(arguments["fileHash"]) == digest
        ):
            raise ValueError("The revision event does not match the request.")

        block_number = receipt["blockNumber"]
        evidence = registry.functions.getVersion(version_id).call(
            block_identifier=block_number
        )
        previous = registry.functions.getVersion(previous_version_id).call(
            block_identifier=block_number
        )

        if not (
            list(evidence[:5])
            == [snake_id, series_id, version_id, version_number, previous_version_id]
            and evidence[5].lower() == sender.lower()
            and bytes(evidence[6]) == digest
            and evidence[7] == 1
            and list(previous[:4])
            == [snake_id, series_id, previous_version_id, version_number - 1]
            and previous[5].lower() == sender.lower()
            and previous[7] == 2
        ):
            raise ValueError("The revised versions do not match the request.")

        block = client.eth.get_block(block_number)
        issued_at = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
    except Exception:
        raise CertificateTransactionError(
            "The transaction succeeded, but its revision evidence could not "
            "be verified. Do not submit again automatically.",
            transaction_hash=transaction_hex,
            outcome="unverified",
        ) from None

    return {
        "transaction_hash": transaction_hex,
        "receipt_status": 1,
        "issued_at": issued_at,
    }
