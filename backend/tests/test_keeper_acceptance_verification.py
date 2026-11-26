from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock, Mock

import psycopg
import pytest
from hexbytes import HexBytes
from web3 import Web3

from backend import sepolia_business as business
from backend.keeper_transfer_routes import KeeperTransferResolutionResponse

SELLER = "0x" + "1" * 40
BUYER = "0x" + "2" * 40
CONTRACT = "0x" + "3" * 40
OTHER = "0x" + "6" * 40
TX_HASH = "0x" + "4" * 64
BLOCK_HASH = HexBytes("0x" + "5" * 64)
PET = "PET-RESPONSE-TEST"
TRANSFER = "TRANSFER-RESPONSE-TEST"
WHEN = datetime.fromtimestamp(1700000000, tz=timezone.utc)


class Result:
    def __init__(self, row):
        self.row = row

    def fetchone(self):
        return self.row


class Cursor:
    def __init__(self, database):
        self.database = database
        self.result = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def execute(self, sql, parameters=None):
        self.result = self.database.execute(sql, parameters)
        return self

    def fetchone(self):
        return self.result.fetchone()


class Database:
    def __init__(self):
        self.statements = []
        self.has_later = False
        self.transfer = {
            "transfer_id": TRANSFER, "snake_id": PET,
            "from_participant_id": "BREEDER001", "to_participant_id": "BUYER001",
            "from_address": SELLER, "to_address": BUYER, "status": "accepted",
            "initiated_at": WHEN, "resolved_at": WHEN,
            "initiation_transaction_id": 6, "acceptance_transaction_id": 7,
        }
        self.checkpoint = {
            "operation": "accept_keeper_transfer", "business_id": TRANSFER,
            "snake_id": PET, "signer_participant_id": "BUYER001",
            "contract_address": CONTRACT, "transaction_hash": TX_HASH,
            "transaction_nonce": 1, "transaction_status": "confirmed", "receipt_status": 1,
        }
        self.pet = {"current_keeper": BUYER, "transaction_status": "confirmed"}

    def cursor(self, **kwargs):
        return Cursor(self)

    @contextmanager
    def transaction(self):
        snapshot = deepcopy((self.transfer, self.checkpoint, self.pet))
        try:
            yield
        except Exception:
            self.transfer, self.checkpoint, self.pet = snapshot
            raise

    def execute(self, sql, parameters=None):
        text = " ".join(sql.split())
        self.statements.append(text)
        if text.startswith("SELECT"):
            if "AS has_later" in text:
                return Result({"has_later": self.has_later})
            if "SELECT username" in text:
                return Result(("registered_buyer",))
            if "SELECT transfer.*" in text:
                return Result({**self.transfer, "saved_acceptance_hash": TX_HASH})
            if "FROM public.sepolia_keeper_transfers" in text:
                return Result(dict(self.transfer))
            if "FROM public.sepolia_business_transactions" in text:
                return Result(dict(self.checkpoint))
            if "FROM public.sepolia_pet_registrations" in text:
                return Result(dict(self.pet))
        if text.startswith("INSERT INTO public.sepolia_business_transactions"):
            return Result((7,))
        if text.startswith("UPDATE public.sepolia_keeper_transfers"):
            if "SET acceptance_transaction_id=" in text:
                self.transfer["acceptance_transaction_id"] = parameters[0]
            else:
                self.transfer["status"] = "accepted"
                self.transfer["resolved_at"] = parameters[0]
            return Result(None)
        if text.startswith("UPDATE public.sepolia_pet_registrations"):
            self.pet["current_keeper"] = parameters[0]
            return Result(None)
        if text.startswith("UPDATE public.sepolia_business_transactions"):
            self.checkpoint["transaction_status"] = "confirmed"
            self.checkpoint["receipt_status"] = 1
            return Result(None)
        raise AssertionError(text)


@pytest.fixture
def evidence(monkeypatch):
    database = Database()
    live = {"keeper": BUYER, "pending": False}
    tx = {
        "chainId": 11155111, "hash": HexBytes(TX_HASH), "from": BUYER, "to": CONTRACT,
        "nonce": 1, "input": b"mock-input", "blockHash": BLOCK_HASH,
        "gas": 400000, "maxFeePerGas": 1,
    }
    receipt = {
        "status": 1, "transactionHash": HexBytes(TX_HASH), "blockNumber": 100,
        "blockHash": BLOCK_HASH, "gasUsed": 50000,
    }
    client = MagicMock()
    client.eth.chain_id = 11155111
    client.eth.block_number = 101
    client.eth.get_transaction.return_value = tx
    client.eth.get_transaction_receipt.return_value = receipt
    client.eth.get_block.return_value = {"timestamp": int(WHEN.timestamp()), "hash": BLOCK_HASH}
    contract = MagicMock()
    contract.decode_function_input.return_value = (
        SimpleNamespace(fn_name="acceptKeeperTransfer"), {"snakeId": PET},
    )
    contract.functions.getCurrentKeeper.return_value.call.side_effect = lambda **kwargs: live["keeper"]
    contract.functions.getPendingKeeperTransfer.return_value.call.side_effect = lambda **kwargs: (
        SELLER, BUYER, live["pending"],
    )
    contract.events.KeeperTransferAccepted.return_value.process_receipt.return_value = [{
        "address": CONTRACT,
        "args": {"snakeId": Web3.keccak(text=PET), "fromKeeper": SELLER, "recipient": BUYER},
    }]
    monkeypatch.setattr(business, "_client_and_contract", lambda name: (
        client, contract, {}, {"KeeperTransfers": CONTRACT},
    ))
    monkeypatch.setattr(business, "get_sepolia_signer", lambda participant_id: SimpleNamespace(address=BUYER))
    no_sign = Mock(side_effect=AssertionError("Must not sign."))
    no_broadcast = Mock(side_effect=AssertionError("Must not broadcast."))
    monkeypatch.setattr(business, "_prepare_signed_call", no_sign)
    monkeypatch.setattr(business, "_broadcast_and_wait", no_broadcast)
    return SimpleNamespace(
        database=database, live=live, contract=contract, receipt=receipt,
        tx=tx, client=client, no_sign=no_sign, no_broadcast=no_broadcast,
    )


def verify(evidence):
    return business.verify_sepolia_keeper_acceptance(
        evidence.database, participant_id="BUYER001", transaction_hash=TX_HASH,
    )


def recover(evidence):
    return business.recover_sepolia_keeper_acceptance(
        evidence.database, participant_id="BUYER001",
        transfer_id=TRANSFER, transaction_hash=TX_HASH,
    )


def test_normal_accept_response_matches_schema(evidence, monkeypatch):
    evidence.database.transfer["status"] = "pending"
    evidence.database.transfer["acceptance_transaction_id"] = None
    evidence.contract.functions.getCurrentKeeper.return_value.call.side_effect = [SELLER, BUYER]
    evidence.contract.functions.getPendingKeeperTransfer.return_value.call.side_effect = [
        (SELLER, BUYER, True), (SELLER, BUYER, False),
    ]
    monkeypatch.setattr(business, "_prepare_signed_call", Mock(
        return_value=(object(), TX_HASH, 1, 50000, 400000, 400000),
    ))
    monkeypatch.setattr(business, "_broadcast_and_wait", Mock(return_value=evidence.receipt))
    result = business.accept_sepolia_keeper_transfer(
        evidence.database, transfer_id=TRANSFER, participant_id="BUYER001",
    )
    parsed = KeeperTransferResolutionResponse.model_validate(result)
    assert parsed.recipient_username == "registered_buyer"
    assert parsed.status == "accepted"
    assert evidence.database.transfer["status"] == "accepted"


def test_completed_acceptance_verification_is_read_only(evidence):
    result = verify(evidence)
    assert result["historical_verified"] is True
    assert result["database_synced"] is True
    assert result["verified"] is True
    assert result["transaction_hash"] == TX_HASH
    assert all(sql.startswith("SELECT") for sql in evidence.database.statements)
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()


def test_unsynced_acceptance_is_recoverable_and_idempotent(evidence):
    database = evidence.database
    database.transfer.update(status="pending", resolved_at=None)
    database.checkpoint.update(transaction_status="submitted", receipt_status=None)
    database.pet["current_keeper"] = SELLER
    before = verify(evidence)
    assert before["historical_verified"] is True
    assert before["verified"] is False
    assert all(sql.startswith("SELECT") for sql in database.statements)
    result = recover(evidence)
    assert KeeperTransferResolutionResponse.model_validate(result).recipient_username == "registered_buyer"
    assert database.transfer["status"] == "accepted"
    assert database.checkpoint["transaction_status"] == "confirmed"
    assert database.checkpoint["receipt_status"] == 1
    assert database.pet["current_keeper"] == BUYER
    assert not any(sql.startswith("INSERT") for sql in database.statements)
    database.statements.clear()
    assert recover(evidence) == result
    assert all(sql.startswith("SELECT") for sql in database.statements)
    assert verify(evidence)["verified"] is True
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()


def test_later_transfer_does_not_invalidate_history_or_rewind_keeper(evidence):
    evidence.live["keeper"] = OTHER
    evidence.database.pet["current_keeper"] = OTHER
    evidence.database.has_later = True
    result = verify(evidence)
    assert result["status"] == "accepted"
    assert result["historical_verified"] is True
    assert result["database_synced"] is True
    assert result["verified"] is False
    assert result["latest_keeper_address"] == OTHER
    recover(evidence)
    assert evidence.database.pet["current_keeper"] == OTHER
    assert all(sql.startswith("SELECT") for sql in evidence.database.statements)
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()


def test_recovery_does_not_overwrite_newer_unsynced_keeper(evidence):
    evidence.live["keeper"] = OTHER
    evidence.database.has_later = True
    with pytest.raises(business.SepoliaBusinessError, match="newer transfer"):
        recover(evidence)
    assert evidence.database.pet["current_keeper"] == BUYER
    assert all(sql.startswith("SELECT") for sql in evidence.database.statements)


def test_resolved_time_compares_instants_not_timezone_text(evidence):
    evidence.database.transfer["resolved_at"] = WHEN.astimezone(timezone(timedelta(hours=1)))
    assert verify(evidence)["verified"] is True
    recover(evidence)
    assert all(sql.startswith("SELECT") for sql in evidence.database.statements)


def test_failed_receipt_never_recovers_database(evidence):
    evidence.receipt["status"] = 0
    with pytest.raises(business.SepoliaBusinessError, match="Receipt Status"):
        recover(evidence)
    assert all(sql.startswith("SELECT") for sql in evidence.database.statements)
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()


def test_recovery_rolls_back_all_updates_on_database_failure(evidence, monkeypatch):
    database = evidence.database
    database.transfer.update(status="pending", resolved_at=None)
    database.checkpoint.update(transaction_status="submitted", receipt_status=None)
    database.pet["current_keeper"] = SELLER
    before = deepcopy((database.transfer, database.checkpoint, database.pet))
    original_execute = database.execute

    def fail_during_keeper_update(sql, parameters=None):
        if " ".join(sql.split()).startswith("UPDATE public.sepolia_pet_registrations"):
            raise psycopg.OperationalError("Simulated database failure.")
        return original_execute(sql, parameters)

    monkeypatch.setattr(database, "execute", fail_during_keeper_update)
    with pytest.raises(business.SepoliaBusinessError) as error:
        recover(evidence)
    assert error.value.outcome == "storage_error"
    assert (database.transfer, database.checkpoint, database.pet) == before
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()


@pytest.mark.parametrize("operation", ["initiate", "accept", "verify", "recover"])
def test_keeper_routes_return_json_matching_schema(evidence, monkeypatch, operation):
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from backend import sepolia_routes
    from backend.keeper_transfer_routes import KeeperTransferInitiationResponse
    from backend.session_routes import CurrentAccountResponse, read_current_account

    accepted = business._keeper_acceptance_evidence(
        evidence.database, transfer=dict(evidence.database.transfer), participant_id="BUYER001",
    )["response"]
    initiated = {**accepted, "status": "pending", "resolved_at": None, "current_keeper_address": SELLER}

    @contextmanager
    def fake_database():
        yield evidence.database

    monkeypatch.setattr(sepolia_routes, "_database", fake_database)
    initiate, accept = Mock(return_value=initiated), Mock(return_value=accepted)
    monkeypatch.setattr(sepolia_routes, "initiate_sepolia_keeper_transfer", initiate)
    monkeypatch.setattr(sepolia_routes, "accept_sepolia_keeper_transfer", accept)
    app = FastAPI()
    app.include_router(sepolia_routes.router)
    seller = operation == "initiate"
    account = CurrentAccountResponse(
        account_id=1, username="seller" if seller else "registered_buyer",
        display_name="Seller" if seller else "Buyer", role="breeder" if seller else "buyer",
        participant_id="BREEDER001" if seller else "BUYER001",
    )
    app.dependency_overrides[read_current_account] = lambda: account
    with TestClient(app, client=("127.0.0.1", 52000), raise_server_exceptions=False) as client:
        if operation == "initiate":
            response = client.post(f"/api/v1/sepolia/snakes/{PET}/keeper-transfers", json={"recipient_username": "registered_buyer"})
        elif operation == "accept":
            response = client.post(f"/api/v1/sepolia/keeper-transfers/{TRANSFER}/accept")
        elif operation == "verify":
            response = client.get("/api/v1/sepolia/keeper-acceptance", params={"transfer_id": TRANSFER})
        else:
            response = client.post("/api/v1/sepolia/keeper-acceptance/recover", json={"transfer_id": TRANSFER, "transaction_hash": TX_HASH})
    assert response.status_code == (201 if seller else 200), response.text
    assert response.headers["content-type"].startswith("application/json")
    schema = KeeperTransferInitiationResponse if seller else KeeperTransferResolutionResponse
    assert schema.model_validate(response.json()).recipient_username == "registered_buyer"
    if operation in {"verify", "recover"}:
        initiate.assert_not_called()
        accept.assert_not_called()
        assert all(sql.startswith("SELECT") for sql in evidence.database.statements)
    evidence.no_sign.assert_not_called()
    evidence.no_broadcast.assert_not_called()

