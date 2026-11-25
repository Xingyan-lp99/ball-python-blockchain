"""Opt-in restart test on a separate port and temporary state directory."""

import hashlib
import json
import os
import socket

import pytest

from backend.demo_chain import BINARY, ROOT, client_for, save_chain, start_chain, stop_chain


@pytest.mark.skipif(os.environ.get("RUN_PERSISTENCE_AUDIT") != "1", reason="Explicit opt-in required")
def test_contracts_receipts_logs_and_pending_transfer_survive_restart(tmp_path):
    with socket.socket() as available:
        available.bind(("127.0.0.1", 0))
        port = available.getsockname()[1]
    start_chain(port, tmp_path, BINARY)
    try:
        client = client_for(port)
        administrator, breeder, lab, _, buyer = client.eth.accounts[:5]

        def deploy(name, *args):
            artifact = json.loads((ROOT / "contracts/artifacts/contracts" / f"{name}.sol" / f"{name}.json").read_text())
            factory = client.eth.contract(abi=artifact["abi"], bytecode=artifact["bytecode"])
            receipt = client.eth.wait_for_transaction_receipt(factory.constructor(*args).transact({"from": administrator}))
            assert receipt.status == 1
            return client.eth.contract(address=receipt.contractAddress, abi=artifact["abi"]), receipt

        snake, deployment = deploy("SnakeRegistry")
        client.eth.wait_for_transaction_receipt(snake.functions.registerSnake("PERSISTENCE_CHECK").transact({"from": breeder}))
        certificate, _ = deploy("CertificateRegistry", snake.address)
        client.eth.wait_for_transaction_receipt(certificate.functions.authorizeLaboratory(lab).transact({"from": administrator}))
        digest = hashlib.sha256(b"isolated restart check").digest()
        issued = client.eth.wait_for_transaction_receipt(certificate.functions.issueCertificate("PERSISTENCE_CHECK", "SERIES", "VERSION", digest).transact({"from": lab}))
        keeper, _ = deploy("KeeperTransfers", snake.address)
        pending = client.eth.wait_for_transaction_receipt(keeper.functions.initiateKeeperTransfer("PERSISTENCE_CHECK", buyer).transact({"from": breeder}))
        block, block_hash = client.eth.block_number, client.eth.get_block("latest").hash
        save_chain(port, tmp_path)
        stop_chain(port, tmp_path)
        start_chain(port, tmp_path, BINARY)
        client = client_for(port)
        assert client.eth.block_number == block
        assert client.eth.get_block("latest").hash == block_hash
        for receipt in (deployment, issued, pending):
            restored = client.eth.get_transaction_receipt(receipt.transactionHash)
            assert restored.status == 1 and restored.blockHash == receipt.blockHash
            assert restored.logs == receipt.logs
            assert client.eth.get_transaction(receipt.transactionHash).hash == receipt.transactionHash
        for contract in (snake, certificate, keeper):
            assert client.eth.get_code(contract.address)
        assert certificate.functions.isAuthorizedLaboratory(lab).call()
        assert bytes(certificate.functions.getVersion("VERSION").call()[6]) == digest
        assert keeper.functions.getCurrentKeeper("PERSISTENCE_CHECK").call() == breeder
        assert keeper.functions.getPendingKeeperTransfer("PERSISTENCE_CHECK").call()[2]
        accepted = client.eth.wait_for_transaction_receipt(keeper.functions.acceptKeeperTransfer("PERSISTENCE_CHECK").transact({"from": buyer}))
        assert accepted.status == 1
        save_chain(port, tmp_path)
        stop_chain(port, tmp_path)
        start_chain(port, tmp_path, BINARY)
        assert keeper.functions.getCurrentKeeper("PERSISTENCE_CHECK").call() == buyer
        assert not keeper.functions.getPendingKeeperTransfer("PERSISTENCE_CHECK").call()[2]
    finally:
        if client_for(port).is_connected():
            stop_chain(port, tmp_path)
