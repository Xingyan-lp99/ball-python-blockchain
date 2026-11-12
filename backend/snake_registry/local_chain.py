"""web3.py adapter for a server-controlled, unlocked LOCAL Hardhat wallet.

No private keys are read, exported, stored, or returned by this application.
Hardhat signs eth_sendTransaction requests on behalf of the demo server.
"""

import json
import os
from pathlib import Path
from urllib.parse import urlparse

from web3 import Web3
from web3.exceptions import BlockNotFound, TransactionNotFound


class ChainUnavailable(Exception):
    pass


class ChainStale(Exception):
    pass


class ChainConflict(Exception):
    pass


def hex_value(value) -> str:
    return Web3.to_hex(value).lower()


class LocalChain:
    def __init__(self) -> None:
        root = Path(__file__).resolve().parents[2]
        path = Path(os.getenv("LOCAL_CHAIN_DEPLOYMENT", str(root / ".local/snake-registry.json")))
        try:
            self.deployment = json.loads(path.read_text(encoding="utf-8"))
            self.chain_id = int(self.deployment["chain_id"])
            self.address = Web3.to_checksum_address(self.deployment["contract_address"])
            self.manager = Web3.to_checksum_address(self.deployment["manager_address"])
            self.instance_id = self.deployment["instance_id"].lower()
            rpc_url = os.getenv("LOCAL_CHAIN_RPC_URL", "http://127.0.0.1:8545")
            parsed = urlparse(rpc_url)
            if (
                self.chain_id != 31337 or parsed.scheme != "http"
                or parsed.hostname not in {"127.0.0.1", "localhost", "host.docker.internal"}
                or parsed.username or parsed.password
            ):
                raise ValueError("Local development only")
            self.web3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={"timeout": 3}))
            self.contract = self.web3.eth.contract(address=self.address, abi=self.deployment["abi"])
        except (OSError, ValueError, KeyError, TypeError):
            raise ChainUnavailable from None

    def validate_scope(self) -> None:
        if not self.web3.client_version.startswith("HardhatNetwork/"):
            raise ChainStale
        if self.web3.eth.chain_id != 31337:
            raise ChainStale
        code = self.web3.eth.get_code(self.address)
        if not code or hex_value(Web3.keccak(code)) != self.deployment["runtime_code_hash"].lower():
            raise ChainStale
        if hex_value(self.contract.functions.instanceId().call()) != self.instance_id:
            raise ChainStale
        try:
            anchor = self.web3.eth.get_block(self.deployment["deployment_block_number"])
        except BlockNotFound:
            raise ChainStale from None
        if hex_value(anchor["hash"]) != self.deployment["deployment_block_hash"].lower():
            raise ChainStale

    def manager_of(self, snake_id: str) -> str | None:
        address = self.contract.functions.managerOf(snake_id).call()
        return None if int(address, 16) == 0 else address

    def transaction_parameters(self) -> tuple[int, int, int]:
        if self.manager not in self.web3.eth.accounts:
            raise ChainUnavailable
        return (
            self.web3.eth.get_transaction_count(self.manager, "pending"),
            self.web3.eth.gas_price,
            self.web3.eth.block_number,
        )

    def send(self, snake_id: str, nonce: int, gas_price: int) -> str:
        # Persist these parameters before broadcasting. Retries send the same
        # transaction with the same nonce, gas price, calldata and signer.
        transaction_hash = self.contract.functions.register(snake_id).transact({
            "from": self.manager, "nonce": nonce, "gas": 300_000,
            "gasPrice": gas_price, "value": 0, "chainId": self.chain_id,
        })
        return hex_value(transaction_hash)

    def receipt(self, transaction_hash: str):
        try:
            return self.web3.eth.get_transaction_receipt(transaction_hash)
        except TransactionNotFound:
            return None

    def registration_hash(self, snake_id: str) -> str | None:
        events = self.contract.events.SnakeRegistered().get_logs(
            from_block=self.deployment["deployment_block_number"], to_block="latest"
        )
        for event in events:
            if event["args"]["snakeId"] == snake_id:
                if event["args"]["manager"].lower() != self.manager.lower():
                    raise ChainConflict
                return hex_value(event["transactionHash"])
        return None

    def recover_hash(self, nonce: int, start_block: int, snake_id: str) -> str | None:
        # Covers a lost send response or a DB failure before saving its hash,
        # including pending transactions and reverted transactions without events.
        blocks = ["pending", *range(start_block, self.web3.eth.block_number + 1)]
        for block_id in blocks:
            block = self.web3.eth.get_block(block_id, full_transactions=True)
            for transaction in block["transactions"]:
                if transaction["from"].lower() == self.manager.lower() and transaction["nonce"] == nonce:
                    self.check_transaction(transaction, snake_id)
                    return hex_value(transaction["hash"])
        if self.web3.eth.get_transaction_count(self.manager, "latest") > nonce:
            raise ChainConflict
        return None

    def check_transaction(self, transaction, snake_id: str) -> None:
        if (
            transaction["from"].lower() != self.manager.lower()
            or (transaction["to"] or "").lower() != self.address.lower()
        ):
            raise ChainConflict
        function, arguments = self.contract.decode_function_input(transaction["input"])
        if function.fn_name != "register" or arguments["snakeId"] != snake_id:
            raise ChainConflict

    def verify_success(self, snake_id: str, transaction_hash: str, receipt) -> None:
        self.check_transaction(self.web3.eth.get_transaction(transaction_hash), snake_id)
        block = self.web3.eth.get_block(receipt["blockNumber"])
        if hex_value(block["hash"]) != hex_value(receipt["blockHash"]):
            raise ChainStale
        events = self.contract.events.SnakeRegistered().process_receipt(receipt)
        if not any(
            event["address"].lower() == self.address.lower()
            and event["args"]["snakeId"] == snake_id
            and event["args"]["manager"].lower() == self.manager.lower()
            for event in events
        ):
            raise ChainConflict
        if (self.manager_of(snake_id) or "").lower() != self.manager.lower():
            raise ChainConflict


def get_local_chain() -> LocalChain:
    return LocalChain()
