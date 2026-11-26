import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import psycopg
from psycopg.rows import dict_row
from eth_abi import decode as abi_decode
from requests.exceptions import RequestException
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractCustomError, ContractLogicError, TimeExhausted, Web3Exception

from backend.certificate_files import (
    get_certificate_pdf_path,
    save_certificate_pdf,
    validate_certificate_pdf,
)
from backend.sepolia_registry import (
    EXPECTED_CHAIN_ID,
    MAX_FEE_PER_GAS,
    SEPOLIA_STATE_PATH,
    _read_env_file,
    get_sepolia_signer,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATHS = {
    "SnakeRegistry": ROOT / "contracts/artifacts/contracts/SnakeRegistry.sol/SnakeRegistry.json",
    "CertificateRegistry": ROOT / "contracts/artifacts/contracts/CertificateRegistry.sol/CertificateRegistry.json",
    "KeeperTransfers": ROOT / "contracts/artifacts/contracts/KeeperTransfers.sol/KeeperTransfers.json",
}
GAS_CAPS = {
    "register_pet": 200_000,
    "issue_certificate": 3_500_000,
    "revise_certificate": 2_700_000,
    "initiate_keeper_transfer": 400_000,
    "accept_keeper_transfer": 400_000,
}


class SepoliaBusinessError(RuntimeError):
    def __init__(
        self, message: str, *, outcome: str = "not_submitted",
        transaction_hash: str | None = None, business_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.outcome = outcome
        self.transaction_hash = transaction_hash
        self.business_id = business_id


def _deployment_state() -> tuple[dict, dict[str, str]]:
    try:
        state = json.loads(SEPOLIA_STATE_PATH.read_text(encoding="utf-8"))
        if state["identity"]["chain_id"] != EXPECTED_CHAIN_ID:
            raise ValueError
        addresses = {}
        for name, artifact_path in ARTIFACT_PATHS.items():
            artifact_bytes = artifact_path.read_bytes()
            artifact = json.loads(artifact_bytes)
            if hashlib.sha256(artifact_bytes).hexdigest() != state["identity"]["artifacts"][name]:
                raise ValueError
            step = next(item for item in state["steps"] if item["name"] == name)
            if step["status"] != "confirmed":
                raise ValueError
            address = step["evidence"]["contract_address"]
            if not Web3.is_address(address) or not artifact.get("abi"):
                raise ValueError
            addresses[name] = Web3.to_checksum_address(address)
    except (OSError, ValueError, KeyError, TypeError, StopIteration):
        raise SepoliaBusinessError(
            "The saved Sepolia deployment checkpoint or Artifact does not match.",
        ) from None
    return state, addresses


def _client_and_contract(name: str) -> tuple[Web3, Contract, dict, dict[str, str]]:
    if name not in ARTIFACT_PATHS:
        raise SepoliaBusinessError("The requested Sepolia contract is not configured.")
    state, addresses = _deployment_state()
    values = _read_env_file()
    try:
        client = Web3(Web3.HTTPProvider(
            values["SEPOLIA_RPC_URL"], request_kwargs={"timeout": 20},
            exception_retry_configuration=None,
        ))
        if not client.is_connected() or client.eth.chain_id != EXPECTED_CHAIN_ID:
            raise ValueError
        for address in addresses.values():
            if not client.eth.get_code(address):
                raise ValueError
        artifact = json.loads(ARTIFACT_PATHS[name].read_text(encoding="utf-8"))
        contract = client.eth.contract(address=addresses[name], abi=artifact["abi"])
        snake_address = addresses["SnakeRegistry"]
        if name != "SnakeRegistry" and contract.functions.snakeRegistry().call().lower() != snake_address.lower():
            raise ValueError
        if name == "CertificateRegistry":
            expected_labs = state["identity"]["laboratories"]
            seller = Web3.to_checksum_address(state["identity"]["seller"])
            if contract.functions.administrator().call() != seller:
                raise ValueError
            if not all(contract.functions.isAuthorizedLaboratory(address).call() for address in expected_labs):
                raise ValueError
    except SepoliaBusinessError:
        raise
    except (OSError, ValueError, KeyError, RequestException, Web3Exception):
        raise SepoliaBusinessError("Sepolia contract or dependency verification failed.") from None
    return client, contract, state, addresses


def _prepare_signed_call(
    *, client: Web3, function, signer, operation: str,
) -> tuple[object, str, int, int, int, int]:
    if client.eth.chain_id != EXPECTED_CHAIN_ID:
        raise SepoliaBusinessError("Unexpected Sepolia Chain ID.")
    latest_nonce = client.eth.get_transaction_count(signer.address, "latest")
    pending_nonce = client.eth.get_transaction_count(signer.address, "pending")
    if latest_nonce != pending_nonce:
        raise SepoliaBusinessError("This wallet has a pending transaction; check it before continuing.")
    latest_block = client.eth.get_block("latest")
    priority_fee = client.eth.max_priority_fee
    max_fee = 2 * latest_block["baseFeePerGas"] + priority_fee
    if not 0 < priority_fee <= max_fee <= MAX_FEE_PER_GAS:
        raise SepoliaBusinessError("Current Sepolia fee quote exceeds the 1 Gwei limit.")
    try:
        estimated_gas = function.estimate_gas({"from": signer.address})
    except (ContractCustomError, Web3Exception, ValueError):
        raise SepoliaBusinessError("The Sepolia contract rejected or could not estimate this operation.") from None
    gas_limit = (estimated_gas * 120 + 99) // 100
    gas_cap = GAS_CAPS[operation]
    if gas_limit > gas_cap:
        raise SepoliaBusinessError(f"Estimated Gas Limit {gas_limit} exceeds this operation's {gas_cap} limit.")
    max_cost = gas_limit * max_fee
    if client.eth.get_balance(signer.address) < max_cost:
        raise SepoliaBusinessError("The signing wallet balance is below the estimated maximum cost.")
    try:
        transaction = function.build_transaction({
            "from": signer.address, "chainId": EXPECTED_CHAIN_ID,
            "nonce": latest_nonce, "value": 0, "gas": gas_limit,
            "maxFeePerGas": max_fee, "maxPriorityFeePerGas": priority_fee,
        })
        signed = signer.sign_transaction(transaction)
        tx_hash = signed.hash.to_0x_hex()
    except (Web3Exception, ValueError, TypeError):
        raise SepoliaBusinessError("The transaction could not be signed; no transaction was sent.") from None
    return signed, tx_hash, latest_nonce, estimated_gas, gas_limit, max_cost


def _broadcast_and_wait(
    *, client: Web3, signed, tx_hash: str, nonce: int,
    max_cost: int, signer, transaction_id: int,
    connection: psycopg.Connection,
) -> dict:
    try:
        if (
            client.eth.chain_id != EXPECTED_CHAIN_ID
            or client.eth.get_transaction_count(signer.address, "pending") != nonce
            or client.eth.get_balance(signer.address) < max_cost
        ):
            raise SepoliaBusinessError(
                "Chain, nonce, or balance changed after checkpointing; do not resubmit.",
                outcome="unknown", transaction_hash=tx_hash,
            )
        returned_hash = client.eth.send_raw_transaction(signed.raw_transaction).to_0x_hex()
        if returned_hash.lower() != tx_hash.lower():
            raise SepoliaBusinessError(
                "RPC returned a different transaction Hash; inspect the saved Hash.",
                outcome="unknown", transaction_hash=tx_hash,
            )
        with connection.transaction():
            connection.execute(
                "UPDATE public.sepolia_business_transactions SET transaction_status='submitted', updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s",
                (transaction_id,),
            )
        receipt = client.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        if receipt["status"] != 1:
            with connection.transaction():
                connection.execute(
                    "UPDATE public.sepolia_business_transactions SET transaction_status='failed', receipt_status=0, updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s",
                    (transaction_id,),
                )
            raise SepoliaBusinessError(
                "The transaction Receipt failed.", outcome="failed", transaction_hash=tx_hash,
            )
        return receipt
    except SepoliaBusinessError as error:
        if error.transaction_hash and error.outcome == "unknown":
            try:
                with connection.transaction():
                    connection.execute(
                        "UPDATE public.sepolia_business_transactions SET transaction_status='unknown',updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s AND transaction_status='prepared'",
                        (transaction_id,),
                    )
            except psycopg.Error:
                pass
        raise
    except (RequestException, TimeExhausted, Web3Exception, psycopg.Error, ValueError):
        try:
            with connection.transaction():
                connection.execute(
                    "UPDATE public.sepolia_business_transactions SET transaction_status='unknown', updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s AND transaction_status <> 'confirmed'",
                    (transaction_id,),
                )
        except psycopg.Error:
            pass
        raise SepoliaBusinessError(
            "Transaction result is unknown. Check the saved Hash; it will not be resent.",
            outcome="unknown", transaction_hash=tx_hash,
        ) from None


def _save_transaction_checkpoint(
    connection: psycopg.Connection, *, operation: str, business_id: str,
    snake_id: str, participant_id: str, contract_address: str,
    tx_hash: str, nonce: int,
) -> int:
    with connection.transaction():
        row = connection.execute(
            """INSERT INTO public.sepolia_business_transactions (
                operation,business_id,snake_id,signer_participant_id,contract_address,
                transaction_hash,transaction_nonce,transaction_status
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,'prepared') RETURNING transaction_id""",
            (operation, business_id, snake_id, participant_id, contract_address, tx_hash, nonce),
        ).fetchone()
    return row[0]


def _mark_confirmed(connection: psycopg.Connection, transaction_id: int) -> None:
    with connection.transaction():
        connection.execute(
            "UPDATE public.sepolia_business_transactions SET transaction_status='confirmed', receipt_status=1, updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s",
            (transaction_id,),
        )


def _transaction_response(
    *, tx_hash: str, contract_address: str, result: dict,
    estimated_gas: int, gas_limit: int, max_fee: int, max_cost: int,
) -> dict:
    return {
        **result, "transaction_hash": tx_hash, "receipt_status": 1,
        "contract_address": contract_address,
        "etherscan_url": f"https://sepolia.etherscan.io/tx/{tx_hash}",
        "chain_id": EXPECTED_CHAIN_ID, "estimated_gas": estimated_gas,
        "gas_limit": gas_limit, "max_fee_per_gas": max_fee,
        "max_cost_wei": max_cost,
    }


def issue_certificate_on_sepolia(
    connection: psycopg.Connection, *, participant_id: str, snake_id: str,
    title: str, pdf_content: bytes,
) -> dict:
    validate_certificate_pdf(pdf_content)
    pet = connection.execute(
        "SELECT 1 FROM public.sepolia_pet_registrations WHERE snake_id=%s AND transaction_status='confirmed'",
        (snake_id,),
    ).fetchone()
    if pet is None:
        raise LookupError("Pet ID is not registered in the Sepolia demo database.")
    lab = connection.execute(
        "SELECT laboratory_id FROM public.laboratories WHERE participant_id=%s",
        (participant_id,),
    ).fetchone()
    if lab is None:
        raise PermissionError("The signed-in laboratory is not configured.")
    signer = get_sepolia_signer(participant_id)
    client, contract, state, addresses = _client_and_contract("CertificateRegistry")
    if not contract.functions.isAuthorizedLaboratory(signer.address).call():
        raise PermissionError("This laboratory is not authorized on Sepolia.")
    try:
        client.eth.contract(
            address=addresses["SnakeRegistry"],
            abi=json.loads(ARTIFACT_PATHS["SnakeRegistry"].read_text(encoding="utf-8"))["abi"],
        ).functions.getCurrentKeeper(snake_id).call()
    except (ContractCustomError, Web3Exception):
        raise LookupError("Pet ID is not registered in the deployed SnakeRegistry.") from None
    series_id = f"SERIES-{uuid4().hex}"
    version_id = f"VERSION-{uuid4().hex}"
    file_hash = hashlib.sha256(pdf_content).hexdigest()
    function = contract.functions.issueCertificate(
        snake_id, series_id, version_id, bytes.fromhex(file_hash),
    )
    signed, tx_hash, nonce, estimate, gas_limit, max_cost = _prepare_signed_call(
        client=client, function=function, signer=signer, operation="issue_certificate",
    )
    max_fee = max_cost // gas_limit
    file_reference, saved_hash = save_certificate_pdf(pdf_content)
    if saved_hash != file_hash:
        raise SepoliaBusinessError("The stored PDF checksum changed; nothing was broadcast.")
    try:
        with connection.transaction():
            tx_row = connection.execute(
                """INSERT INTO public.sepolia_business_transactions (
                    operation,business_id,snake_id,signer_participant_id,contract_address,
                    transaction_hash,transaction_nonce,transaction_status
                ) VALUES ('issue_certificate',%s,%s,%s,%s,%s,%s,'prepared') RETURNING transaction_id""",
                (series_id, snake_id, participant_id, addresses["CertificateRegistry"], tx_hash, nonce),
            ).fetchone()
            connection.execute(
                "INSERT INTO public.sepolia_certificate_series(series_id,snake_id,laboratory_id,title) VALUES (%s,%s,%s,%s)",
                (series_id, snake_id, lab[0], title.strip()),
            )
            connection.execute(
                """INSERT INTO public.sepolia_certificate_versions(
                    version_id,series_id,version_number,previous_version_id,file_reference,
                    file_hash,issuer_address,status,transaction_id
                ) VALUES (%s,%s,1,NULL,%s,%s,%s,NULL,%s)""",
                (version_id, series_id, file_reference, file_hash, signer.address, tx_row[0]),
            )
    except psycopg.Error:
        raise SepoliaBusinessError("The transaction checkpoint could not be saved; nothing was broadcast.") from None
    receipt = _broadcast_and_wait(
        client=client, signed=signed, tx_hash=tx_hash, nonce=nonce,
        max_cost=max_cost, signer=signer, transaction_id=tx_row[0], connection=connection,
    )
    try:
        logs = contract.events.CertificateIssued().process_receipt(receipt)
        if len(logs) != 1:
            raise ValueError
        event = logs[0]["args"]
        evidence = contract.functions.getVersion(version_id).call(block_identifier=receipt["blockNumber"])
        if not (
            event["snakeId"] == snake_id and event["issuer"].lower() == signer.address.lower()
            and event["versionNumber"] == 1 and bytes(event["fileHash"]) == bytes.fromhex(file_hash)
            and evidence[0] == snake_id and evidence[1] == series_id and evidence[2] == version_id
            and evidence[3] == 1 and evidence[5].lower() == signer.address.lower()
            and bytes(evidence[6]) == bytes.fromhex(file_hash) and evidence[7] == 1
        ):
            raise ValueError
        issued_at = datetime.fromtimestamp(client.eth.get_block(receipt["blockNumber"])["timestamp"], tz=timezone.utc)
        with connection.transaction():
            connection.execute(
                "UPDATE public.sepolia_certificate_versions SET status=1,issued_at=%s WHERE version_id=%s",
                (issued_at, version_id),
            )
            connection.execute(
                "UPDATE public.sepolia_business_transactions SET transaction_status='confirmed',receipt_status=1,updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s",
                (tx_row[0],),
            )
    except (ValueError, Web3Exception, psycopg.Error, KeyError, IndexError):
        raise SepoliaBusinessError(
            "The Receipt succeeded but certificate evidence or database status could not be verified.",
            outcome="unverified", transaction_hash=tx_hash, business_id=series_id,
        ) from None
    return _transaction_response(
        tx_hash=tx_hash, contract_address=addresses["CertificateRegistry"],
        result={"snake_id": snake_id, "laboratory_id": lab[0], "title": title.strip(),
                "series_id": series_id, "version_id": version_id, "version_number": 1,
                "file_hash": file_hash, "issuer_address": signer.address,
                "status": "current", "issued_at": issued_at},
        estimated_gas=estimate, gas_limit=gas_limit, max_fee=max_fee, max_cost=max_cost,
    )


def revise_certificate_on_sepolia(
    connection: psycopg.Connection, *, participant_id: str, series_id: str,
    pdf_content: bytes,
) -> dict:
    validate_certificate_pdf(pdf_content)
    lab = connection.execute(
        "SELECT laboratory_id FROM public.laboratories WHERE participant_id=%s",
        (participant_id,),
    ).fetchone()
    if lab is None:
        raise PermissionError("The signed-in laboratory is not configured.")
    series = connection.execute(
        "SELECT snake_id,laboratory_id,title FROM public.sepolia_certificate_series WHERE series_id=%s",
        (series_id,),
    ).fetchone()
    if series is None:
        raise LookupError("Sepolia certificate series not found.")
    snake_id, laboratory_id, title = series
    if laboratory_id != lab[0]:
        raise PermissionError("Only the issuing laboratory may revise this certificate.")
    previous = connection.execute(
        """SELECT version_id,version_number,file_hash,issuer_address FROM public.sepolia_certificate_versions
           WHERE series_id=%s AND status=1 ORDER BY version_number DESC LIMIT 1""",
        (series_id,),
    ).fetchone()
    if previous is None:
        raise SepoliaBusinessError("The certificate series has no confirmed Current version.")
    signer = get_sepolia_signer(participant_id)
    client, contract, _, addresses = _client_and_contract("CertificateRegistry")
    if previous[3].lower() != signer.address.lower():
        raise PermissionError("Only the original issuing wallet may revise this certificate.")
    previous_evidence = contract.functions.getVersion(previous[0]).call()
    if previous_evidence[7] != 1 or previous_evidence[5].lower() != signer.address.lower():
        raise SepoliaBusinessError("On-chain Current version or issuer does not match the saved record.")
    version_id = f"VERSION-{uuid4().hex}"
    version_number = previous[1] + 1
    file_hash = hashlib.sha256(pdf_content).hexdigest()
    function = contract.functions.appendRevision(series_id, version_id, bytes.fromhex(file_hash))
    signed, tx_hash, nonce, estimate, gas_limit, max_cost = _prepare_signed_call(
        client=client, function=function, signer=signer, operation="revise_certificate",
    )
    max_fee = max_cost // gas_limit
    file_reference, saved_hash = save_certificate_pdf(pdf_content)
    if saved_hash != file_hash:
        raise SepoliaBusinessError("The stored PDF checksum changed; nothing was broadcast.")
    try:
        with connection.transaction():
            tx_row = connection.execute(
                """INSERT INTO public.sepolia_business_transactions(
                    operation,business_id,snake_id,signer_participant_id,contract_address,
                    transaction_hash,transaction_nonce,transaction_status
                ) VALUES ('revise_certificate',%s,%s,%s,%s,%s,%s,'prepared') RETURNING transaction_id""",
                (version_id, snake_id, participant_id, addresses["CertificateRegistry"], tx_hash, nonce),
            ).fetchone()
            connection.execute(
                """INSERT INTO public.sepolia_certificate_versions(
                    version_id,series_id,version_number,previous_version_id,file_reference,
                    file_hash,issuer_address,status,transaction_id
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,NULL,%s)""",
                (version_id, series_id, version_number, previous[0], file_reference,
                 file_hash, signer.address, tx_row[0]),
            )
    except psycopg.Error:
        raise SepoliaBusinessError("The revision checkpoint could not be saved; nothing was broadcast.") from None
    receipt = _broadcast_and_wait(
        client=client, signed=signed, tx_hash=tx_hash, nonce=nonce,
        max_cost=max_cost, signer=signer, transaction_id=tx_row[0], connection=connection,
    )
    try:
        logs = contract.events.CertificateRevised().process_receipt(receipt)
        if len(logs) != 1:
            raise ValueError
        event = logs[0]["args"]
        evidence = contract.functions.getVersion(version_id).call(block_identifier=receipt["blockNumber"])
        old_evidence = contract.functions.getVersion(previous[0]).call(block_identifier=receipt["blockNumber"])
        if not (
            event["issuer"].lower() == signer.address.lower()
            and event["versionNumber"] == version_number
            and bytes(event["fileHash"]) == bytes.fromhex(file_hash)
            and evidence[0] == snake_id and evidence[1] == series_id and evidence[2] == version_id
            and evidence[3] == version_number and evidence[4] == previous[0]
            and evidence[5].lower() == signer.address.lower()
            and bytes(evidence[6]) == bytes.fromhex(file_hash) and evidence[7] == 1
            and old_evidence[7] == 2
        ):
            raise ValueError
        issued_at = datetime.fromtimestamp(client.eth.get_block(receipt["blockNumber"])["timestamp"], tz=timezone.utc)
        with connection.transaction():
            connection.execute("UPDATE public.sepolia_certificate_versions SET status=2 WHERE version_id=%s", (previous[0],))
            connection.execute("UPDATE public.sepolia_certificate_versions SET status=1,issued_at=%s WHERE version_id=%s", (issued_at, version_id))
            connection.execute("UPDATE public.sepolia_business_transactions SET transaction_status='confirmed',receipt_status=1,updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s", (tx_row[0],))
    except (ValueError, Web3Exception, psycopg.Error, KeyError, IndexError):
        raise SepoliaBusinessError(
            "The Receipt succeeded but revision evidence or database status could not be verified.",
            outcome="unverified", transaction_hash=tx_hash, business_id=version_id,
        ) from None
    return _transaction_response(
        tx_hash=tx_hash, contract_address=addresses["CertificateRegistry"],
        result={"snake_id": snake_id, "laboratory_id": laboratory_id, "title": title,
                "series_id": series_id, "version_id": version_id, "version_number": version_number,
                "previous_version_id": previous[0], "previous_version_status": "superseded",
                "file_hash": file_hash, "issuer_address": signer.address,
                "status": "current", "issued_at": issued_at},
        estimated_gas=estimate, gas_limit=gas_limit, max_fee=max_fee, max_cost=max_cost,
    )


def recover_sepolia_certificate_transaction(
    connection: psycopg.Connection, *, participant_id: str, transaction_hash: str,
) -> dict:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """SELECT * FROM public.sepolia_business_transactions
               WHERE transaction_hash=%s""",
            (transaction_hash,),
        )
        checkpoint = cursor.fetchone()
    if checkpoint is None or checkpoint["signer_participant_id"] != participant_id:
        raise PermissionError("This laboratory cannot recover the requested transaction.")
    operation = checkpoint["operation"]
    if operation not in {"issue_certificate", "revise_certificate"}:
        raise LookupError("No certificate transaction checkpoint was found.")

    state, addresses = _deployment_state()
    lab_addresses = {
        "LAB001": state["identity"]["laboratories"][0],
        "LAB002": state["identity"]["laboratories"][1],
    }
    expected_issuer = Web3.to_checksum_address(lab_addresses.get(participant_id, ""))
    client, contract, _, loaded_addresses = _client_and_contract("CertificateRegistry")
    if checkpoint["contract_address"].lower() != loaded_addresses["CertificateRegistry"].lower():
        raise SepoliaBusinessError(
            "The saved certificate checkpoint targets a different contract.",
            outcome="unverified", transaction_hash=transaction_hash,
            business_id=checkpoint["business_id"],
        )

    with connection.cursor(row_factory=dict_row) as cursor:
        if operation == "issue_certificate":
            cursor.execute(
                """SELECT s.series_id,s.snake_id,s.laboratory_id,s.title,
                          v.version_id,v.version_number,v.previous_version_id,
                          v.file_reference,v.file_hash,v.issuer_address,v.status,v.issued_at
                   FROM public.sepolia_certificate_series AS s
                   JOIN public.sepolia_certificate_versions AS v
                     ON v.transaction_id=%s AND v.series_id=s.series_id
                   WHERE s.series_id=%s""",
                (checkpoint["transaction_id"], checkpoint["business_id"]),
            )
        else:
            cursor.execute(
                """SELECT s.series_id,s.snake_id,s.laboratory_id,s.title,
                          v.version_id,v.version_number,v.previous_version_id,
                          v.file_reference,v.file_hash,v.issuer_address,v.status,v.issued_at
                   FROM public.sepolia_certificate_versions AS v
                   JOIN public.sepolia_certificate_series AS s USING(series_id)
                   WHERE v.transaction_id=%s AND v.version_id=%s""",
                (checkpoint["transaction_id"], checkpoint["business_id"]),
            )
        record = cursor.fetchone()
    if record is None:
        raise SepoliaBusinessError(
            "The saved certificate record does not match its transaction checkpoint.",
            outcome="unverified", transaction_hash=transaction_hash,
            business_id=checkpoint["business_id"],
        )

    try:
        if (
            checkpoint["snake_id"] != record["snake_id"]
            or checkpoint["transaction_status"] not in {"prepared", "submitted", "unknown", "confirmed"}
            or checkpoint["receipt_status"] not in {None, 1}
            or record["laboratory_id"] != participant_id
            or record["issuer_address"].lower() != expected_issuer.lower()
            or not contract.functions.isAuthorizedLaboratory(expected_issuer).call()
        ):
            raise ValueError

        pdf_path = get_certificate_pdf_path(record["file_reference"])
        if pdf_path is None:
            raise ValueError
        pdf_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
        if pdf_hash != record["file_hash"]:
            raise ValueError

        tx = client.eth.get_transaction(transaction_hash)
        receipt = client.eth.get_transaction_receipt(transaction_hash)
        if (
            client.eth.chain_id != EXPECTED_CHAIN_ID
            or tx["chainId"] != EXPECTED_CHAIN_ID
            or tx["hash"].to_0x_hex().lower() != transaction_hash.lower()
            or tx["from"].lower() != expected_issuer.lower()
            or tx["to"].lower() != loaded_addresses["CertificateRegistry"].lower()
            or receipt["status"] != 1
            or receipt["transactionHash"].to_0x_hex().lower() != transaction_hash.lower()
        ):
            raise ValueError

        function, arguments = contract.decode_function_input(tx["input"])
        if operation == "issue_certificate":
            event_name = "CertificateIssued"
            expected_call = (
                function.fn_name == "issueCertificate"
                and arguments.get("snakeId") == record["snake_id"]
                and arguments.get("seriesId") == record["series_id"]
                and arguments.get("versionId") == record["version_id"]
                and bytes(arguments.get("fileHash", b"")) == bytes.fromhex(pdf_hash)
                and record["version_number"] == 1
                and record["previous_version_id"] is None
            )
        else:
            event_name = "CertificateRevised"
            expected_call = (
                function.fn_name == "appendRevision"
                and arguments.get("seriesId") == record["series_id"]
                and arguments.get("versionId") == record["version_id"]
                and bytes(arguments.get("fileHash", b"")) == bytes.fromhex(pdf_hash)
                and record["version_number"] >= 2
                and bool(record["previous_version_id"])
            )
        if not expected_call:
            raise ValueError

        logs = getattr(contract.events, event_name)().process_receipt(receipt)
        if len(logs) != 1:
            raise ValueError
        event = logs[0]["args"]
        evidence = contract.functions.getVersion(record["version_id"]).call(
            block_identifier=receipt["blockNumber"]
        )
        current_evidence = contract.functions.getVersion(record["version_id"]).call()
        common_event_valid = (
            bytes(event["seriesId"]) == Web3.keccak(text=record["series_id"])
            and bytes(event["versionId"]) == Web3.keccak(text=record["version_id"])
            and event["issuer"].lower() == expected_issuer.lower()
            and event["versionNumber"] == record["version_number"]
            and bytes(event["fileHash"]) == bytes.fromhex(pdf_hash)
        )
        evidence_valid = (
            evidence[0] == record["snake_id"]
            and evidence[1] == record["series_id"]
            and evidence[2] == record["version_id"]
            and evidence[3] == record["version_number"]
            and evidence[5].lower() == expected_issuer.lower()
            and bytes(evidence[6]) == bytes.fromhex(pdf_hash)
            and evidence[7] == 1
            and current_evidence[7] == 1
        )
        previous = None
        if operation == "revise_certificate":
            previous = contract.functions.getVersion(record["previous_version_id"]).call(
                block_identifier=receipt["blockNumber"]
            )
            previous_latest = contract.functions.getVersion(record["previous_version_id"]).call()
            evidence_valid = (
                evidence_valid
                and evidence[4] == record["previous_version_id"]
                and previous[7] == 2
                and previous_latest[7] == 2
            )
            common_event_valid = (
                common_event_valid
                and bytes(event["previousVersionId"])
                == Web3.keccak(text=record["previous_version_id"])
            )
        if not (common_event_valid and evidence_valid):
            raise ValueError

        issued_at = datetime.fromtimestamp(
            client.eth.get_block(receipt["blockNumber"])["timestamp"], tz=timezone.utc,
        )
        with connection.transaction():
            cursor = connection.cursor(row_factory=dict_row)
            cursor.execute(
                "SELECT transaction_hash,transaction_status,receipt_status "
                "FROM public.sepolia_business_transactions WHERE transaction_id=%s FOR UPDATE",
                (checkpoint["transaction_id"],),
            )
            locked_checkpoint = cursor.fetchone()
            cursor.execute(
                "SELECT status,previous_version_id,issuer_address,file_hash "
                "FROM public.sepolia_certificate_versions WHERE version_id=%s FOR UPDATE",
                (record["version_id"],),
            )
            locked_version = cursor.fetchone()
            if not (
                locked_checkpoint
                and locked_checkpoint["transaction_hash"].lower() == transaction_hash.lower()
                and locked_checkpoint["transaction_status"] in {"prepared", "submitted", "unknown", "confirmed"}
                and locked_checkpoint["receipt_status"] in {None, 1}
                and locked_version
                and locked_version["previous_version_id"] == record["previous_version_id"]
                and locked_version["issuer_address"].lower() == expected_issuer.lower()
                and locked_version["file_hash"] == pdf_hash
                and locked_version["status"] in {None, 1}
            ):
                raise ValueError

            if operation == "revise_certificate":
                connection.execute(
                    "UPDATE public.sepolia_certificate_versions SET status=2 WHERE version_id=%s",
                    (record["previous_version_id"],),
                )
            connection.execute(
                """UPDATE public.sepolia_certificate_versions
                   SET status=1,issued_at=COALESCE(issued_at,%s) WHERE version_id=%s""",
                (issued_at, record["version_id"]),
            )
            connection.execute(
                """UPDATE public.sepolia_business_transactions
                   SET transaction_status='confirmed',receipt_status=1,
                       updated_at=CURRENT_TIMESTAMP
                   WHERE transaction_id=%s AND transaction_hash=%s""",
                (checkpoint["transaction_id"], transaction_hash),
            )

        max_fee = tx.get("maxFeePerGas", tx.get("gasPrice", 0))
        result = {
            "snake_id": record["snake_id"],
            "laboratory_id": record["laboratory_id"],
            "title": record["title"],
            "series_id": record["series_id"],
            "version_id": record["version_id"],
            "version_number": record["version_number"],
            "file_hash": pdf_hash,
            "issuer_address": expected_issuer,
            "status": "current",
            "issued_at": record["issued_at"] or issued_at,
        }
        if operation == "revise_certificate":
            result.update({
                "previous_version_id": record["previous_version_id"],
                "previous_version_status": "superseded",
            })
        return _transaction_response(
            tx_hash=transaction_hash,
            contract_address=loaded_addresses["CertificateRegistry"],
            result=result,
            estimated_gas=receipt["gasUsed"],
            gas_limit=tx["gas"],
            max_fee=max_fee,
            max_cost=tx["gas"] * max_fee,
        )
    except (KeyError, IndexError, TypeError, ValueError, Web3Exception, psycopg.Error):
        raise SepoliaBusinessError(
            "The saved certificate transaction could not be fully verified; no new transaction was sent.",
            outcome="unverified",
            transaction_hash=transaction_hash,
            business_id=checkpoint["business_id"],
        ) from None


def list_sepolia_laboratory_reports(connection: psycopg.Connection, *, participant_id: str) -> list[dict]:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """SELECT series.series_id,series.snake_id,series.title,series.laboratory_id,
                      COALESCE(MAX(version.version_number) FILTER (WHERE tx.transaction_status='confirmed'),0) AS latest_version_number
               FROM public.sepolia_certificate_series AS series
               JOIN public.laboratories AS lab USING (laboratory_id)
               LEFT JOIN public.sepolia_certificate_versions AS version USING (series_id)
               LEFT JOIN public.sepolia_business_transactions AS tx USING (transaction_id)
               WHERE lab.participant_id=%s
               GROUP BY series.series_id ORDER BY series.title,series.snake_id""",
            (participant_id,),
        )
        return list(cursor.fetchall())


def sepolia_keeper_state(connection: psycopg.Connection, *, snake_id: str) -> dict:
    pet = connection.execute(
        "SELECT transaction_status FROM public.sepolia_pet_registrations WHERE snake_id=%s",
        (snake_id,),
    ).fetchone()
    if pet is None or pet[0] != "confirmed":
        raise LookupError("Pet ID is not registered in the Sepolia demo database.")
    client, contract, _, _ = _client_and_contract("KeeperTransfers")
    try:
        block_number = client.eth.block_number
        keeper = contract.functions.getCurrentKeeper(snake_id).call(block_identifier=block_number)
        from_address, to_address, pending = contract.functions.getPendingKeeperTransfer(snake_id).call(block_identifier=block_number)
    except (ContractCustomError, RequestException, Web3Exception):
        raise SepoliaBusinessError("Live Keeper state could not be confirmed from Sepolia.", outcome="unknown") from None
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """SELECT transfer_id,status,from_participant_id,to_participant_id,initiated_at,resolved_at,
                      initiation_transaction_id,acceptance_transaction_id
               FROM public.sepolia_keeper_transfers WHERE snake_id=%s
               ORDER BY COALESCE(resolved_at,initiated_at) DESC NULLS LAST LIMIT 1""",
            (snake_id,),
        )
        transfer = cursor.fetchone()
        if transfer:
            cursor.execute(
                "SELECT transaction_hash,transaction_status FROM public.sepolia_business_transactions WHERE transaction_id=%s",
                (transfer["acceptance_transaction_id"] or transfer["initiation_transaction_id"],),
            )
            tx = cursor.fetchone()
        else:
            tx = None
    return {
        "snake_id": snake_id,
        "current_keeper_address": keeper,
        "pending": pending,
        "from_keeper_address": from_address if pending else None,
        "recipient_address": to_address if pending else None,
        "transfer": transfer,
        "transaction_hash": tx["transaction_hash"] if tx else None,
        "transaction_status": tx["transaction_status"] if tx else None,
        "block_number": block_number,
    }


def initiate_sepolia_keeper_transfer(
    connection: psycopg.Connection, *, snake_id: str,
    participant_id: str, recipient_username: str,
) -> dict:
    state = sepolia_keeper_state(connection, snake_id=snake_id)
    sender = get_sepolia_signer(participant_id)
    if sender.address.lower() != state["current_keeper_address"].lower():
        raise PermissionError("Only the current Sepolia Keeper may initiate this transfer.")
    recipient_row = connection.execute(
        """SELECT accounts.participant_id,accounts.username FROM public.user_accounts AS accounts
           WHERE LOWER(accounts.username)=LOWER(%s) AND accounts.role='buyer'""",
        (recipient_username.strip(),),
    ).fetchone()
    if recipient_row is None:
        raise LookupError("Registered Buyer account not found.")
    recipient_id, recipient_name = recipient_row
    recipient = get_sepolia_signer(recipient_id)
    if recipient.address.lower() == sender.address.lower():
        raise ValueError("Buyer and current Keeper must be different Sepolia wallets.")
    if state["pending"]:
        raise ValueError("A Sepolia Keeper transfer is already pending.")
    client, contract, _, addresses = _client_and_contract("KeeperTransfers")
    transfer_id = f"TRANSFER-{uuid4().hex}"
    function = contract.functions.initiateKeeperTransfer(snake_id, recipient.address)
    signed, tx_hash, nonce, estimate, gas_limit, max_cost = _prepare_signed_call(
        client=client, function=function, signer=sender, operation="initiate_keeper_transfer",
    )
    max_fee = max_cost // gas_limit
    try:
        with connection.transaction():
            tx_row = connection.execute(
                """INSERT INTO public.sepolia_business_transactions(
                    operation,business_id,snake_id,signer_participant_id,contract_address,
                    transaction_hash,transaction_nonce,transaction_status
                ) VALUES ('initiate_keeper_transfer',%s,%s,%s,%s,%s,%s,'prepared') RETURNING transaction_id""",
                (transfer_id, snake_id, participant_id, addresses["KeeperTransfers"], tx_hash, nonce),
            ).fetchone()
            connection.execute(
                """INSERT INTO public.sepolia_keeper_transfers(
                    transfer_id,snake_id,from_participant_id,to_participant_id,from_address,to_address,
                    status,initiation_transaction_id
                ) VALUES (%s,%s,%s,%s,%s,%s,'prepared',%s)""",
                (transfer_id, snake_id, participant_id, recipient_id, sender.address, recipient.address, tx_row[0]),
            )
    except psycopg.Error:
        raise SepoliaBusinessError("Transfer checkpoint could not be saved; nothing was broadcast.") from None
    receipt = _broadcast_and_wait(client=client, signed=signed, tx_hash=tx_hash, nonce=nonce, max_cost=max_cost, signer=sender, transaction_id=tx_row[0], connection=connection)
    try:
        logs = contract.events.KeeperTransferInitiated().process_receipt(receipt)
        live_keeper = contract.functions.getCurrentKeeper(snake_id).call(block_identifier=receipt["blockNumber"])
        from_address, to_address, pending = contract.functions.getPendingKeeperTransfer(snake_id).call(block_identifier=receipt["blockNumber"])
        if not (len(logs) == 1 and logs[0]["args"]["fromKeeper"].lower() == sender.address.lower()
                and logs[0]["args"]["recipient"].lower() == recipient.address.lower()
                and live_keeper.lower() == sender.address.lower() and pending
                and from_address.lower() == sender.address.lower() and to_address.lower() == recipient.address.lower()):
            raise ValueError
        initiated_at = datetime.fromtimestamp(client.eth.get_block(receipt["blockNumber"])["timestamp"], tz=timezone.utc)
        with connection.transaction():
            connection.execute("UPDATE public.sepolia_keeper_transfers SET status='pending',initiated_at=%s WHERE transfer_id=%s", (initiated_at, transfer_id))
            connection.execute("UPDATE public.sepolia_business_transactions SET transaction_status='confirmed',receipt_status=1,updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s", (tx_row[0],))
    except (ValueError, Web3Exception, psycopg.Error, KeyError, IndexError):
        raise SepoliaBusinessError("Transfer Receipt succeeded but its chain/database state could not be verified.", outcome="unverified", transaction_hash=tx_hash, business_id=transfer_id) from None
    return _transaction_response(
        tx_hash=tx_hash, contract_address=addresses["KeeperTransfers"],
        result={"transfer_id": transfer_id, "snake_id": snake_id,
                "from_participant_id": participant_id, "to_participant_id": recipient_id,
                "recipient_username": recipient_name, "current_keeper_address": sender.address,
                "status": "pending", "initiated_at": initiated_at, "resolved_at": None},
        estimated_gas=estimate, gas_limit=gas_limit, max_fee=max_fee, max_cost=max_cost,
    )


def _keeper_recipient_username(connection, participant_id: str) -> str:
    row = connection.execute(
        "SELECT username FROM public.user_accounts WHERE participant_id=%s",
        (participant_id,),
    ).fetchone()
    if row is None or not isinstance(row[0], str) or not row[0].strip():
        raise ValueError("The transfer recipient has no registered username.")
    return row[0]


def _keeper_acceptance_response(*, recipient_username: str, **kwargs) -> dict:
    # Import only when called, after route and business modules have initialized.
    from backend.keeper_transfer_routes import KeeperTransferResolutionResponse

    payload = _transaction_response(**kwargs)
    payload["recipient_username"] = recipient_username
    try:
        return KeeperTransferResolutionResponse.model_validate(payload).model_dump(mode="json")
    except ValueError:
        raise SepoliaBusinessError(
            "Acceptance response schema validation failed. Verify the saved transaction; do not submit again.",
            outcome="unverified", transaction_hash=payload.get("transaction_hash"),
            business_id=payload.get("transfer_id"),
        ) from None


def _same_keeper_time(value, expected: datetime) -> bool:
    return (
        isinstance(value, datetime) and value.utcoffset() is not None
        and value.astimezone(timezone.utc) == expected.astimezone(timezone.utc)
    )


def _saved_keeper_acceptance(
    connection: psycopg.Connection, *, participant_id: str,
    transfer_id: str | None = None, transaction_hash: str | None = None,
) -> dict:
    if not transfer_id and not transaction_hash:
        raise ValueError("Provide a transfer ID or acceptance transaction Hash.")
    condition = "transfer.transfer_id=%s" if transfer_id else "LOWER(tx.transaction_hash)=LOWER(%s)"
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            f"""SELECT transfer.*, tx.transaction_hash AS saved_acceptance_hash
                FROM public.sepolia_keeper_transfers AS transfer
                LEFT JOIN public.sepolia_business_transactions AS tx
                  ON tx.transaction_id=transfer.acceptance_transaction_id
                WHERE {condition}""",
            (transfer_id or transaction_hash,),
        )
        transfer = cursor.fetchone()
    if transfer is None:
        raise LookupError("No saved transfer matches the supplied identifier.")
    if transfer["to_participant_id"] != participant_id:
        raise PermissionError("Only the designated Buyer may inspect this acceptance.")
    saved_hash = transfer.get("saved_acceptance_hash")
    if not transfer["acceptance_transaction_id"] or not saved_hash:
        raise SepoliaBusinessError(
            "No acceptance checkpoint exists. No transaction was sent.",
            outcome="unverified", business_id=transfer["transfer_id"],
        )
    if transaction_hash and saved_hash.lower() != transaction_hash.lower():
        raise SepoliaBusinessError(
            "The supplied Hash is not this transfer's acceptance Hash.",
            outcome="unverified", transaction_hash=transaction_hash,
            business_id=transfer["transfer_id"],
        )
    return transfer


def _keeper_acceptance_evidence(
    connection: psycopg.Connection, *, transfer: dict, participant_id: str,
) -> dict:
    """Read historical acceptance evidence and a separate latest-state snapshot."""
    transfer_id, snake_id = transfer["transfer_id"], transfer["snake_id"]
    if transfer["to_participant_id"] != participant_id:
        raise PermissionError("Only the designated Buyer may inspect this acceptance.")
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            "SELECT * FROM public.sepolia_business_transactions WHERE transaction_id=%s",
            (transfer["acceptance_transaction_id"],),
        )
        checkpoint = cursor.fetchone()
    tx_hash = checkpoint["transaction_hash"] if checkpoint else None

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise SepoliaBusinessError(
                message, outcome="unverified", transaction_hash=tx_hash, business_id=transfer_id,
            )

    require(checkpoint is not None, "The acceptance checkpoint is missing.")
    try:
        require(
            checkpoint["operation"] == "accept_keeper_transfer"
            and checkpoint["business_id"] == transfer_id
            and checkpoint["snake_id"] == snake_id
            and checkpoint["signer_participant_id"] == participant_id,
            "The checkpoint identity does not match this acceptance.",
        )
        require(
            checkpoint["transaction_status"] in {"prepared", "submitted", "unknown", "confirmed"}
            and checkpoint["receipt_status"] in {None, 1}
            and transfer["status"] in {"pending", "accepted"},
            "The saved transaction or transfer state conflicts with acceptance.",
        )
        username = _keeper_recipient_username(connection, participant_id)
        client, contract, _, addresses = _client_and_contract("KeeperTransfers")
        contract_address = addresses["KeeperTransfers"]
        require(
            checkpoint["contract_address"].lower() == contract_address.lower(),
            "The checkpoint targets a different KeeperTransfers contract.",
        )
        tx, receipt = client.eth.get_transaction(tx_hash), client.eth.get_transaction_receipt(tx_hash)
        require(
            client.eth.chain_id == EXPECTED_CHAIN_ID and tx["chainId"] == EXPECTED_CHAIN_ID
            and tx["hash"].to_0x_hex().lower() == tx_hash.lower()
            and receipt["transactionHash"].to_0x_hex().lower() == tx_hash.lower(),
            "The transaction or Receipt identity does not match the checkpoint.",
        )
        require(
            tx["from"].lower() == transfer["to_address"].lower()
            and tx["to"].lower() == contract_address.lower()
            and tx["nonce"] == checkpoint["transaction_nonce"],
            "The signer, target contract, or nonce does not match the checkpoint.",
        )
        require(receipt["status"] == 1, "The acceptance Receipt Status is not 1.")
        block = client.eth.get_block(receipt["blockNumber"])
        require(
            block["hash"] == receipt["blockHash"] and tx["blockHash"] == receipt["blockHash"],
            "The Receipt is not in the expected canonical block.",
        )
        function, arguments = contract.decode_function_input(tx["input"])
        require(
            function.fn_name == "acceptKeeperTransfer" and arguments.get("snakeId") == snake_id,
            "The transaction does not accept this Pet ID.",
        )
        logs = contract.events.KeeperTransferAccepted().process_receipt(receipt)
        require(len(logs) == 1, "Expected exactly one acceptance event.")
        event = logs[0]
        require(
            event["address"].lower() == contract_address.lower()
            and bytes(event["args"]["snakeId"]) == Web3.keccak(text=snake_id)
            and event["args"]["fromKeeper"].lower() == transfer["from_address"].lower()
            and event["args"]["recipient"].lower() == transfer["to_address"].lower(),
            "The acceptance event does not match this transfer.",
        )
        # A later transaction, even in the same block, cannot invalidate this event.
        latest_block = client.eth.block_number
        latest_keeper = contract.functions.getCurrentKeeper(snake_id).call(block_identifier=latest_block)
        latest_pending = contract.functions.getPendingKeeperTransfer(snake_id).call(block_identifier=latest_block)[2]
        resolved_at = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
        max_fee = tx.get("maxFeePerGas", tx.get("gasPrice", 0))
        response = _keeper_acceptance_response(
            recipient_username=username, tx_hash=tx_hash, contract_address=contract_address,
            result={
                "transfer_id": transfer_id, "snake_id": snake_id,
                "from_participant_id": transfer["from_participant_id"], "to_participant_id": participant_id,
                "current_keeper_address": transfer["to_address"], "status": "accepted",
                "initiated_at": transfer["initiated_at"], "resolved_at": resolved_at,
            },
            estimated_gas=receipt["gasUsed"], gas_limit=tx["gas"],
            max_fee=max_fee, max_cost=tx["gas"] * max_fee,
        )
        return {
            "response": response, "checkpoint": checkpoint, "resolved_at": resolved_at,
            "latest_keeper": latest_keeper, "latest_pending": latest_pending,
            "latest_block": latest_block,
        }
    except SepoliaBusinessError:
        raise
    except (KeyError, IndexError, TypeError, ValueError, OSError, RequestException, Web3Exception, psycopg.Error):
        raise SepoliaBusinessError(
            "Acceptance evidence could not be read or decoded. No transaction was sent.",
            outcome="unverified", transaction_hash=tx_hash, business_id=transfer_id,
        ) from None


def _recover_sepolia_keeper_acceptance(
    connection: psycopg.Connection, *, transfer: dict, participant_id: str,
) -> dict:
    evidence = _keeper_acceptance_evidence(connection, transfer=transfer, participant_id=participant_id)
    response, checkpoint = evidence["response"], evidence["checkpoint"]
    resolved_at = evidence["resolved_at"]
    transfer_id, snake_id = transfer["transfer_id"], transfer["snake_id"]
    transaction_id, tx_hash = transfer["acceptance_transaction_id"], response["transaction_hash"]

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise SepoliaBusinessError(
                message, outcome="unverified", transaction_hash=tx_hash, business_id=transfer_id,
            )

    try:
        with connection.transaction():
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    "SELECT * FROM public.sepolia_keeper_transfers WHERE transfer_id=%s FOR UPDATE", (transfer_id,),
                )
                locked_transfer = cursor.fetchone()
                cursor.execute(
                    "SELECT current_keeper,transaction_status FROM public.sepolia_pet_registrations WHERE snake_id=%s FOR UPDATE",
                    (snake_id,),
                )
                pet = cursor.fetchone()
                cursor.execute(
                    "SELECT * FROM public.sepolia_business_transactions WHERE transaction_id=%s FOR UPDATE", (transaction_id,),
                )
                locked_tx = cursor.fetchone()
                require(
                    locked_transfer is not None
                    and all(locked_transfer[field] == transfer[field] for field in (
                        "snake_id", "from_participant_id", "to_participant_id", "from_address",
                        "to_address", "initiation_transaction_id", "acceptance_transaction_id",
                    ))
                    and locked_transfer["status"] in {"pending", "accepted"},
                    "The transfer changed during recovery.",
                )
                require(
                    locked_tx is not None
                    and all(locked_tx[field] == checkpoint[field] for field in (
                        "operation", "business_id", "snake_id", "signer_participant_id",
                        "contract_address", "transaction_hash", "transaction_nonce",
                    ))
                    and locked_tx["transaction_status"] in {"prepared", "submitted", "unknown", "confirmed"}
                    and locked_tx["receipt_status"] in {None, 1},
                    "The acceptance checkpoint changed during recovery.",
                )
                require(
                    pet is not None and pet["transaction_status"] == "confirmed"
                    and isinstance(pet["current_keeper"], str),
                    "The pet registration is not ready for recovery.",
                )
                require(
                    locked_transfer["resolved_at"] is None
                    or _same_keeper_time(locked_transfer["resolved_at"], resolved_at),
                    "The saved resolution time conflicts with the Receipt block.",
                )
                need_keeper_update = pet["current_keeper"].lower() != evidence["latest_keeper"].lower()
                if need_keeper_update:
                    cursor.execute(
                        """SELECT EXISTS (
                               SELECT 1 FROM public.sepolia_keeper_transfers
                               WHERE snake_id=%s AND transfer_id<>%s AND initiation_transaction_id>%s
                           ) AS has_later""",
                        (snake_id, transfer_id, locked_transfer["initiation_transaction_id"]),
                    )
                    has_later = cursor.fetchone()["has_later"]
                    require(
                        not has_later and evidence["latest_keeper"].lower() == transfer["to_address"].lower()
                        and evidence["latest_pending"] is False
                        and pet["current_keeper"].lower() in {transfer["from_address"].lower(), transfer["to_address"].lower()},
                        "The database Keeper differs from the latest chain state. "
                        "This recovery will not overwrite a newer transfer.",
                    )
                if locked_transfer["status"] != "accepted" or locked_transfer["resolved_at"] is None:
                    connection.execute(
                        """UPDATE public.sepolia_keeper_transfers SET status='accepted',resolved_at=%s
                           WHERE transfer_id=%s AND acceptance_transaction_id=%s""",
                        (resolved_at, transfer_id, transaction_id),
                    )
                if need_keeper_update:
                    connection.execute(
                        """UPDATE public.sepolia_pet_registrations
                           SET current_keeper=%s,updated_at=CURRENT_TIMESTAMP WHERE snake_id=%s""",
                        (evidence["latest_keeper"], snake_id),
                    )
                if locked_tx["transaction_status"] != "confirmed" or locked_tx["receipt_status"] != 1:
                    connection.execute(
                        """UPDATE public.sepolia_business_transactions
                           SET transaction_status='confirmed',receipt_status=1,updated_at=CURRENT_TIMESTAMP
                           WHERE transaction_id=%s AND transaction_hash=%s""",
                        (transaction_id, tx_hash),
                    )
        return response
    except SepoliaBusinessError:
        raise
    except (KeyError, TypeError, ValueError, psycopg.Error):
        raise SepoliaBusinessError(
            "Database recovery could not be completed. No transaction was signed or broadcast.",
            outcome="storage_error", transaction_hash=tx_hash, business_id=transfer_id,
        ) from None


def verify_sepolia_keeper_acceptance(
    connection: psycopg.Connection, *, participant_id: str,
    transfer_id: str | None = None, transaction_hash: str | None = None,
) -> dict:
    transfer = _saved_keeper_acceptance(
        connection, participant_id=participant_id, transfer_id=transfer_id, transaction_hash=transaction_hash,
    )
    evidence = _keeper_acceptance_evidence(connection, transfer=transfer, participant_id=participant_id)
    checkpoint = evidence["checkpoint"]
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            "SELECT current_keeper,transaction_status FROM public.sepolia_pet_registrations WHERE snake_id=%s",
            (transfer["snake_id"],),
        )
        pet = cursor.fetchone()
    problems = []
    if transfer["status"] != "accepted":
        problems.append("The database transfer is not accepted.")
    if checkpoint["transaction_status"] != "confirmed" or checkpoint["receipt_status"] != 1:
        problems.append("The acceptance checkpoint is not confirmed with Receipt Status 1.")
    if not _same_keeper_time(transfer["resolved_at"], evidence["resolved_at"]):
        problems.append("The database resolution time does not match the Receipt block.")
    if not (
        pet and pet["transaction_status"] == "confirmed" and isinstance(pet["current_keeper"], str)
        and pet["current_keeper"].lower() == evidence["latest_keeper"].lower()
    ):
        problems.append("The database Keeper does not match the latest chain Keeper.")
    database_synced = not problems
    still_current = evidence["latest_keeper"].lower() == transfer["to_address"].lower() and evidence["latest_pending"] is False
    if not still_current:
        problems.append(
            "This historical acceptance is confirmed, but a later Keeper change "
            "or pending transfer exists. It is not proof of the current transfer state."
        )
    return {
        **evidence["response"], "historical_verified": True, "database_synced": database_synced,
        "verified": database_synced and still_current, "latest_keeper_address": evidence["latest_keeper"],
        "latest_pending": evidence["latest_pending"], "chain_block_number": evidence["latest_block"],
        "detail": " ".join(problems) or None,
    }


def recover_sepolia_keeper_acceptance(
    connection: psycopg.Connection, *, participant_id: str,
    transfer_id: str | None = None, transaction_hash: str | None = None,
) -> dict:
    transfer = _saved_keeper_acceptance(
        connection, participant_id=participant_id, transfer_id=transfer_id, transaction_hash=transaction_hash,
    )
    return _recover_sepolia_keeper_acceptance(connection, transfer=transfer, participant_id=participant_id)


def accept_sepolia_keeper_transfer(
    connection: psycopg.Connection, *, transfer_id: str, participant_id: str,
) -> dict:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute("SELECT * FROM public.sepolia_keeper_transfers WHERE transfer_id=%s", (transfer_id,))
        transfer = cursor.fetchone()
    if transfer is None:
        raise LookupError("Sepolia Keeper transfer not found.")
    if transfer["to_participant_id"] != participant_id:
        raise PermissionError("Only the designated Buyer may accept this transfer.")
    if transfer["acceptance_transaction_id"] is not None:
        return _recover_sepolia_keeper_acceptance(
            connection, transfer=transfer, participant_id=participant_id,
        )
    if transfer["status"] != "pending":
        raise ValueError("This transfer is not available for acceptance.")
    recipient_username = _keeper_recipient_username(connection, participant_id)
    signer = get_sepolia_signer(participant_id)
    if signer.address.lower() != transfer["to_address"].lower():
        raise PermissionError("The active Sepolia Buyer wallet does not match the recipient.")
    client, contract, _, addresses = _client_and_contract("KeeperTransfers")
    current = contract.functions.getCurrentKeeper(transfer["snake_id"]).call()
    from_address, to_address, pending = contract.functions.getPendingKeeperTransfer(transfer["snake_id"]).call()
    if not (pending and current.lower() == transfer["from_address"].lower()
            and from_address.lower() == transfer["from_address"].lower()
            and to_address.lower() == transfer["to_address"].lower()):
        raise ValueError("The saved transfer does not match the live Sepolia pending state.")
    function = contract.functions.acceptKeeperTransfer(transfer["snake_id"])
    signed, tx_hash, nonce, estimate, gas_limit, max_cost = _prepare_signed_call(
        client=client, function=function, signer=signer, operation="accept_keeper_transfer",
    )
    max_fee = max_cost // gas_limit
    try:
        with connection.transaction():
            tx_row = connection.execute(
                """INSERT INTO public.sepolia_business_transactions(
                    operation,business_id,snake_id,signer_participant_id,contract_address,
                    transaction_hash,transaction_nonce,transaction_status
                ) VALUES ('accept_keeper_transfer',%s,%s,%s,%s,%s,%s,'prepared') RETURNING transaction_id""",
                (transfer_id, transfer["snake_id"], participant_id, addresses["KeeperTransfers"], tx_hash, nonce),
            ).fetchone()
            connection.execute("UPDATE public.sepolia_keeper_transfers SET acceptance_transaction_id=%s WHERE transfer_id=%s", (tx_row[0], transfer_id))
    except psycopg.Error:
        raise SepoliaBusinessError("Acceptance checkpoint could not be saved; nothing was broadcast.") from None
    receipt = _broadcast_and_wait(client=client, signed=signed, tx_hash=tx_hash, nonce=nonce, max_cost=max_cost, signer=signer, transaction_id=tx_row[0], connection=connection)
    try:
        logs = contract.events.KeeperTransferAccepted().process_receipt(receipt)
        current = contract.functions.getCurrentKeeper(transfer["snake_id"]).call(block_identifier=receipt["blockNumber"])
        _, _, pending = contract.functions.getPendingKeeperTransfer(transfer["snake_id"]).call(block_identifier=receipt["blockNumber"])
        if not (len(logs) == 1 and current.lower() == signer.address.lower() and not pending
                and logs[0]["args"]["fromKeeper"].lower() == transfer["from_address"].lower()
                and logs[0]["args"]["recipient"].lower() == signer.address.lower()):
            raise ValueError
        resolved_at = datetime.fromtimestamp(client.eth.get_block(receipt["blockNumber"])["timestamp"], tz=timezone.utc)
        response = _keeper_acceptance_response(
            recipient_username=recipient_username,
            tx_hash=tx_hash, contract_address=addresses["KeeperTransfers"],
            result={"transfer_id": transfer_id, "snake_id": transfer["snake_id"],
                    "from_participant_id": transfer["from_participant_id"],
                    "to_participant_id": participant_id, "current_keeper_address": signer.address,
                    "status": "accepted", "initiated_at": transfer["initiated_at"], "resolved_at": resolved_at},
            estimated_gas=estimate, gas_limit=gas_limit, max_fee=max_fee, max_cost=max_cost,
        )
        with connection.transaction():
            connection.execute("UPDATE public.sepolia_keeper_transfers SET status='accepted',resolved_at=%s WHERE transfer_id=%s", (resolved_at, transfer_id))
            connection.execute("UPDATE public.sepolia_pet_registrations SET current_keeper=%s,updated_at=CURRENT_TIMESTAMP WHERE snake_id=%s", (signer.address, transfer["snake_id"]))
            connection.execute("UPDATE public.sepolia_business_transactions SET transaction_status='confirmed',receipt_status=1,updated_at=CURRENT_TIMESTAMP WHERE transaction_id=%s", (tx_row[0],))
    except (ValueError, Web3Exception, psycopg.Error, KeyError, IndexError):
        raise SepoliaBusinessError("Acceptance Receipt succeeded but Current Keeper or database state could not be verified.", outcome="unverified", transaction_hash=tx_hash, business_id=transfer_id) from None
    return response


def certificate_pdf_reference(connection: psycopg.Connection, *, version_id: str) -> str | None:
    row = connection.execute(
        "SELECT file_reference FROM public.sepolia_certificate_versions WHERE version_id=%s AND status IN (1,2)",
        (version_id,),
    ).fetchone()
    return row[0] if row else None


def sepolia_certificate_history(connection: psycopg.Connection, *, snake_id: str) -> list[dict]:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """SELECT s.series_id,s.title,s.laboratory_id,v.version_id,v.version_number,
                      v.previous_version_id,v.file_hash,v.issuer_address,v.issued_at,v.status,
                      t.transaction_status,t.transaction_hash
               FROM public.sepolia_certificate_series AS s
               JOIN public.sepolia_certificate_versions AS v USING(series_id)
               JOIN public.sepolia_business_transactions AS t USING(transaction_id)
               WHERE s.snake_id=%s ORDER BY s.laboratory_id,s.series_id,v.version_number""",
            (snake_id,),
        )
        return list(cursor.fetchall())


def simulate_unauthorized_lab_call(*, snake_id: str) -> str:
    client, contract, _, _ = _client_and_contract("CertificateRegistry")
    unauthorized = Web3.to_checksum_address("0x000000000000000000000000000000000000dEaD")
    try:
        contract.functions.issueCertificate(
            snake_id, "UNAUTHORIZED-SIMULATION", "UNAUTHORIZED-SIMULATION-V1", b"\x00" * 32,
        ).call({"from": unauthorized})
    except ContractCustomError as error:
        if error.data == Web3.keccak(text="Unauthorized()")[:4].hex() or error.data == Web3.to_hex(Web3.keccak(text="Unauthorized()")[:4]):
            return "The Sepolia contract rejected an unauthorized Laboratory call (eth_call only; no transaction was sent)."
        raise SepoliaBusinessError("The contract reverted, but not with the expected Unauthorized error.") from None
    except ContractLogicError as error:
        if getattr(error, "data", None) == Web3.to_hex(Web3.keccak(text="Unauthorized()")[:4]):
            return "The Sepolia contract rejected an unauthorized Laboratory call (eth_call only; no transaction was sent)."
        raise SepoliaBusinessError("A contract revert occurred, but Unauthorized was not confirmed.") from None
    except Web3Exception:
        raise SepoliaBusinessError("The read-only permission check could not reach Sepolia.") from None
    raise SepoliaBusinessError("The unauthorized simulation unexpectedly succeeded; no transaction was sent.")


def _permission_demo_result(
    *, caller: str, operation: str, authorized: bool | None,
    contract_result: str, revert_reason: str | None, state_unchanged: str,
    series_id: str | None = None,
) -> dict:
    return {
        "network": "Sepolia Testnet",
        "contract": "CertificateRegistry",
        "contract_address": _deployment_state()[1]["CertificateRegistry"],
        "pet_id": "BP-S004",
        "series_id": series_id,
        "simulated_caller": caller,
        "operation": operation,
        "authorization_status": (
            "Authorized" if authorized is True else "Unauthorized"
            if authorized is False else "Unable to Verify"
        ),
        "contract_result": contract_result,
        "revert_reason": revert_reason,
        "state_unchanged": state_unchanged,
        "read_only_notice": "Read-only eth_call. No transaction broadcast. No Gas Fee.",
        "permission_denied": contract_result == "Reverted" and revert_reason is not None,
    }


def _exception_revert_bytes(error: Exception) -> bytes | None:
    candidates = [getattr(error, "data", None), *getattr(error, "args", ())]
    while candidates:
        value = candidates.pop(0)
        if isinstance(value, dict):
            candidates.extend(value.values())
        elif isinstance(value, (bytes, bytearray)) and len(value) >= 4:
            return bytes(value)
        elif isinstance(value, str):
            import re
            match = re.search(r"0x[0-9a-fA-F]{8,}", value)
            if match:
                raw = match.group(0)
                if len(raw) % 2:
                    raw = raw[:-1]
                try:
                    return bytes.fromhex(raw[2:])
                except ValueError:
                    continue
    return None


def _version_exists_for_demo(contract: Contract, version_id: str) -> bool | None:
    try:
        contract.functions.getVersion(version_id).call()
        return True
    except ContractCustomError as error:
        data = _exception_revert_bytes(error)
        if data and data[:4] == Web3.keccak(text="VersionNotFound(string)")[:4]:
            return False
        return None
    except ContractLogicError as error:
        data = _exception_revert_bytes(error)
        if data and data[:4] == Web3.keccak(text="VersionNotFound(string)")[:4]:
            return False
        return None
    except Web3Exception:
        return None


def _permission_call_result(function, *, caller: str, expected_selector: bytes, expected_args: tuple) -> tuple[str, str | None]:
    try:
        function.call({"from": caller})
        return "Allowed", None
    except (ContractCustomError, ContractLogicError) as error:
        data = _exception_revert_bytes(error)
        if not data:
            return "Inconclusive", "The RPC returned a revert without decodable error data."
        if data[:4] != expected_selector:
            return "Inconclusive", f"Unexpected contract error selector: 0x{data[:4].hex()}"
        try:
            decoded = abi_decode(
                [item[0] for item in expected_args], data[4:], strict=True,
            ) if expected_args else ()
        except Exception:
            return "Inconclusive", f"Expected custom error 0x{data[:4].hex()} had invalid arguments."
        for actual, (_, expected, *_) in zip(decoded, expected_args):
            if isinstance(expected, str) and Web3.is_address(expected):
                if Web3.to_checksum_address(actual) != Web3.to_checksum_address(expected):
                    return "Inconclusive", f"Custom error caller or identifier did not match: 0x{data[:4].hex()}"
            elif actual != expected:
                return "Inconclusive", f"Custom error arguments did not match: 0x{data[:4].hex()}"
        if expected_args:
            values = ", ".join(str(value) for value in decoded)
            return "Reverted", f"{expected_args[0][2]}({values})"
        return "Reverted", "Unauthorized()"
    except Web3Exception as error:
        return "Inconclusive", f"Sepolia eth_call failed ({type(error).__name__})."


def run_sepolia_certificate_permission_demo(
    connection: psycopg.Connection, *, operation: str, snake_id: str,
) -> dict:
    base = {
        "network": "Sepolia Testnet", "contract": "CertificateRegistry",
        "contract_address": None, "pet_id": snake_id,
        "series_id": None, "simulated_caller": None,
        "operation": (
            "issueCertificate(string,string,string,bytes32)"
            if operation == "unauthorized_issuance"
            else "appendRevision(string,string,bytes32)"
        ),
        "authorization_status": "Unable to Verify", "contract_result": "Inconclusive",
        "revert_reason": None, "state_unchanged": "Unable to Verify",
        "read_only_notice": "Read-only eth_call. No transaction broadcast. No Gas Fee.",
        "permission_denied": False,
    }
    if snake_id != "BP-S004" or operation not in {"unauthorized_issuance", "cross_lab_revision"}:
        return {**base, "revert_reason": "Only the configured BP-S004 permission demos are supported."}

    try:
        state, addresses = _deployment_state()
        client, contract, _, addresses = _client_and_contract("CertificateRegistry")
        base["contract_address"] = addresses["CertificateRegistry"]
        labs = {
            "LAB001": Web3.to_checksum_address(state["identity"]["laboratories"][0]),
            "LAB002": Web3.to_checksum_address(state["identity"]["laboratories"][1]),
        }
        unauthorized_address = Web3.to_checksum_address(_read_env_file()["SEPOLIA_BUYER_ADDRESS"])
        base["simulated_caller"] = (
            unauthorized_address if operation == "unauthorized_issuance" else labs["LAB002"]
        )
        base["authorization_status"] = (
            "Unauthorized" if operation == "unauthorized_issuance"
            and not contract.functions.isAuthorizedLaboratory(unauthorized_address).call()
            else "Authorized" if operation == "cross_lab_revision"
            and contract.functions.isAuthorizedLaboratory(labs["LAB002"]).call()
            else "Unable to Verify"
        )
        snake_artifact = json.loads(ARTIFACT_PATHS["SnakeRegistry"].read_text(encoding="utf-8"))
        snake = client.eth.contract(address=addresses["SnakeRegistry"], abi=snake_artifact["abi"])
        if not snake.functions.getCurrentKeeper(snake_id).call():
            return {**base, "revert_reason": "The Pet ID is not registered on Sepolia."}

        if operation == "unauthorized_issuance":
            caller = unauthorized_address
            authorized = contract.functions.isAuthorizedLaboratory(caller).call()
            if authorized:
                return _permission_demo_result(
                    caller=caller, operation="issueCertificate(string,string,string,bytes32)",
                    authorized=True, contract_result="Inconclusive",
                    revert_reason="Buyer address is authorized; it is not a valid unauthorized caller.",
                    state_unchanged="Unable to Verify",
                )
            series_id = f"PERMISSION-DEMO-{uuid4().hex}"
            version_id = f"PERMISSION-DEMO-V1-{uuid4().hex}"
            if _version_exists_for_demo(contract, version_id) is not False:
                raise SepoliaBusinessError("Could not confirm unused issuance demo identifiers.")
            db_before = connection.execute(
                "SELECT COUNT(*) FROM public.sepolia_certificate_series WHERE series_id=%s",
                (series_id,),
            ).fetchone()[0]
            version_db_before = connection.execute(
                "SELECT COUNT(*) FROM public.sepolia_certificate_versions WHERE version_id=%s",
                (version_id,),
            ).fetchone()[0]
            if db_before != 0 or version_db_before != 0:
                raise SepoliaBusinessError("The issuance demo identifiers already exist in the database.")
            function = contract.functions.issueCertificate(
                snake_id, series_id, version_id, hashlib.sha256(b"permission demo").digest(),
            )
            result, reason = _permission_call_result(
                function, caller=caller,
                expected_selector=Web3.keccak(text="Unauthorized()")[:4], expected_args=(),
            )
            unchanged = _version_exists_for_demo(contract, version_id) is False
            db_after = connection.execute(
                "SELECT COUNT(*) FROM public.sepolia_certificate_series WHERE series_id=%s",
                (series_id,),
            ).fetchone()[0]
            version_db_after = connection.execute(
                "SELECT COUNT(*) FROM public.sepolia_certificate_versions WHERE version_id=%s",
                (version_id,),
            ).fetchone()[0]
            unchanged = unchanged and db_after == 0 and version_db_after == 0
            output = _permission_demo_result(
                caller=caller, operation="issueCertificate(string,string,string,bytes32)",
                authorized=False, contract_result=result, revert_reason=reason,
                state_unchanged="Yes" if unchanged else "No" if unchanged is False else "Unable to Verify",
            )
            output["series_id"] = series_id
            return output

        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """SELECT series_id,snake_id,laboratory_id,title
                   FROM public.sepolia_certificate_series
                   WHERE snake_id=%s AND title='Gene Test' AND laboratory_id='LAB001'""",
                (snake_id,),
            )
            series_rows = cursor.fetchall()
        if len(series_rows) != 1:
            return {**base, "revert_reason": "Could not identify exactly one LAB001 Gene Test series."}
        series = series_rows[0]
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """SELECT version_id,version_number,previous_version_id,file_hash,
                          issuer_address,status,transaction_status
                   FROM public.sepolia_certificate_versions v
                   JOIN public.sepolia_business_transactions t USING(transaction_id)
                   WHERE v.series_id=%s ORDER BY version_number""",
                (series["series_id"],),
            )
            versions = cursor.fetchall()
        if len(versions) != 2 or [row["version_number"] for row in versions] != [1, 2]:
            return {**base, "series_id": series["series_id"], "revert_reason": "Expected only confirmed V1 and V2 records."}
        v1, v2 = versions
        authorized_lab2 = contract.functions.isAuthorizedLaboratory(labs["LAB002"]).call()
        if not authorized_lab2 or series["laboratory_id"] != "LAB001":
            return {**base, "series_id": series["series_id"], "simulated_caller": labs["LAB002"], "revert_reason": "Laboratory authorization or series ownership precondition failed."}
        chain_v1 = contract.functions.getVersion(v1["version_id"]).call()
        chain_v2 = contract.functions.getVersion(v2["version_id"]).call()
        if not (
            v1["status"] == 2 and v1["transaction_status"] == "confirmed"
            and v2["status"] == 1 and v2["transaction_status"] == "confirmed"
            and v1["issuer_address"].lower() == labs["LAB001"].lower()
            and v2["issuer_address"].lower() == labs["LAB001"].lower()
            and v1["previous_version_id"] is None
            and v2["previous_version_id"] == v1["version_id"]
            and chain_v1[0] == snake_id and chain_v1[1] == series["series_id"]
            and chain_v1[2] == v1["version_id"] and chain_v1[3] == 1
            and chain_v1[4] == "" and bytes(chain_v1[6]).hex() == v1["file_hash"]
            and chain_v1[5].lower() == labs["LAB001"].lower() and chain_v1[7] == 2
            and chain_v2[0] == snake_id and chain_v2[1] == series["series_id"]
            and chain_v2[2] == v2["version_id"] and chain_v2[3] == 2
            and chain_v2[4] == v1["version_id"] and bytes(chain_v2[6]).hex() == v2["file_hash"]
            and chain_v2[5].lower() == labs["LAB001"].lower() and chain_v2[7] == 1
        ):
            return {**base, "series_id": series["series_id"], "simulated_caller": labs["LAB002"], "revert_reason": "V1/V2 chain and database state do not match the required demo precondition."}

        caller = labs["LAB002"]
        new_version_id = f"PERMISSION-DEMO-V3-{uuid4().hex}"
        if _version_exists_for_demo(contract, new_version_id) is not False:
            raise SepoliaBusinessError("Could not confirm an unused V3 demo identifier.")
        function = contract.functions.appendRevision(
            series["series_id"], new_version_id, hashlib.sha256(b"cross-lab revision demo").digest(),
        )
        result, reason = _permission_call_result(
            function, caller=caller,
            expected_selector=Web3.keccak(text="NotSeriesIssuer(string,address)")[:4],
            expected_args=(("string", series["series_id"], "NotSeriesIssuer"), ("address", caller, "NotSeriesIssuer")),
        )
        after_v1 = contract.functions.getVersion(v1["version_id"]).call()
        after_v2 = contract.functions.getVersion(v2["version_id"]).call()
        v3_exists = _version_exists_for_demo(contract, new_version_id)
        db_after_versions = connection.execute(
            """SELECT version_id,version_number,status FROM public.sepolia_certificate_versions
               WHERE series_id=%s ORDER BY version_number""",
            (series["series_id"],),
        ).fetchall()
        db_v3_count = connection.execute(
            "SELECT COUNT(*) FROM public.sepolia_certificate_versions WHERE version_id=%s",
            (new_version_id,),
        ).fetchone()[0]
        unchanged = (
            after_v1[7] == 2 and after_v2[7] == 1 and v3_exists is False
            and v1["status"] == 2 and v2["status"] == 1 and db_v3_count == 0
            and [(r[0], r[1], r[2]) for r in db_after_versions]
            == [(v1["version_id"], 1, 2), (v2["version_id"], 2, 1)]
        )
        output = _permission_demo_result(
            caller=caller, operation="appendRevision(string,string,bytes32)",
            authorized=True, contract_result=result, revert_reason=reason,
            state_unchanged="Yes" if unchanged else "No" if v3_exists is True else "Unable to Verify",
            series_id=series["series_id"],
        )
        output["previous_version_id"] = v1["version_id"]
        output["current_version_id"] = v2["version_id"]
        output["simulated_version_id"] = new_version_id
        return output
    except (SepoliaBusinessError, ContractCustomError, ContractLogicError, Web3Exception, psycopg.Error, KeyError, ValueError, IndexError) as error:
        base["revert_reason"] = f"Inconclusive: {type(error).__name__}."
        return base
