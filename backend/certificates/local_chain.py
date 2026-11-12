import os
from dataclasses import dataclass
from pathlib import Path

from snake_registry.local_chain import LocalChain, ChainConflict, ChainStale, ChainUnavailable, hex_value


@dataclass(frozen=True)
class CertificateSubject:
    certificate_id: str
    snake_id: str
    issuer_address: str
    file_hash: bytes


class CertificatePreflightError(ChainConflict):
    def __init__(self, code: str, detail: str):
        self.code = code
        self.detail = detail


class CertificateChain(LocalChain):
    def __init__(self) -> None:
        root = Path(__file__).resolve().parents[2]
        path = Path(os.getenv("CERTIFICATE_CHAIN_DEPLOYMENT", str(root / ".local/certificate-registry.json")))
        super().__init__(path)
        self.snakes = LocalChain()
        if self.deployment.get("lab_id") != "LAB001" or self.manager.lower() == self.snakes.manager.lower():
            raise ChainUnavailable
        self.lab_name = self.deployment.get("lab_name", "Demo Laboratory LAB001")

    def validate_scope(self) -> None:
        super().validate_scope()
        self.snakes.validate_scope()
        if (
            self.deployment.get("snake_contract_address", "").lower() != self.snakes.address.lower()
            or self.deployment.get("snake_instance_id") != self.snakes.instance_id
            or self.contract.functions.snakeRegistry().call().lower() != self.snakes.address.lower()
        ):
            raise ChainStale

    def assert_can_issue(self, subject: CertificateSubject) -> None:
        if subject.issuer_address.lower() != self.manager.lower():
            raise CertificatePreflightError(
                "issuer_wallet_mismatch",
                f"V1 expects issuer {subject.issuer_address}, but LAB001 currently signs as {self.manager}. The original issuer cannot be overwritten.",
            )
        if not self.contract.functions.authorizedLaboratories(self.manager).call():
            raise CertificatePreflightError(
                "laboratory_not_authorized",
                f"LAB001 wallet {self.manager} is not authorized by CertificateRegistry {self.address}. Only the deployment administrator can authorize it.",
            )
        if self.snakes.manager_of(subject.snake_id) is None:
            raise CertificatePreflightError(
                "snake_not_registered",
                f"Snake {subject.snake_id} is not registered in the referenced SnakeRegistry {self.snakes.address}. Complete its chain registration in the Breeder workspace, then refresh this certificate. No new issuance transaction will be sent until this prerequisite is met.",
            )

    def record(self, certificate_id: str) -> dict | None:
        snake_id, issuer, version, file_hash = self.contract.functions.getVersion(certificate_id, 1).call()
        if version == 0:
            return None
        return {"certificate_id": certificate_id, "snake_id": snake_id,
                "issuer_address": issuer, "version": version, "file_hash": bytes(file_hash)}

    def assert_record(self, subject: CertificateSubject, record: dict) -> None:
        expected = {"certificate_id": subject.certificate_id, "snake_id": subject.snake_id,
                    "issuer_address": subject.issuer_address.lower(), "version": 1, "file_hash": subject.file_hash}
        for field, value in expected.items():
            actual = record[field].lower() if field == "issuer_address" else record[field]
            if actual != value:
                raise CertificatePreflightError(
                    "certificate_record_conflict",
                    f"On-chain V1 for certificate {subject.certificate_id} has a different {field}. Existing V1 records cannot be overwritten.",
                )

    def send(self, subject: CertificateSubject, nonce: int, gas_price: int) -> str:
        return hex_value(self.contract.functions.issueV1(
            subject.certificate_id, subject.snake_id, subject.file_hash
        ).transact({"from": self.manager, "nonce": nonce, "gas": 500_000,
                    "gasPrice": gas_price, "value": 0, "chainId": self.chain_id}))

    def check_transaction(self, transaction, subject: CertificateSubject) -> None:
        if transaction["from"].lower() != subject.issuer_address.lower() or (transaction["to"] or "").lower() != self.address.lower():
            raise ChainConflict
        function, arguments = self.contract.decode_function_input(transaction["input"])
        if (
            function.fn_name != "issueV1" or arguments["certificateId"] != subject.certificate_id
            or arguments["snakeId"] != subject.snake_id or bytes(arguments["fileHash"]) != subject.file_hash
        ):
            raise ChainConflict

    def registration_hash(self, subject: CertificateSubject) -> str | None:
        for event in self.contract.events.CertificateIssued().get_logs(
            from_block=self.deployment["deployment_block_number"], to_block="latest"
        ):
            args = event["args"]
            if args["certificateId"] == subject.certificate_id and args["version"] == 1:
                self.assert_record(subject, {
                    "certificate_id": args["certificateId"], "snake_id": args["snakeId"],
                    "issuer_address": args["issuer"], "version": args["version"], "file_hash": bytes(args["fileHash"]),
                })
                return hex_value(event["transactionHash"])
        return None

    def verify_success(self, subject: CertificateSubject, transaction_hash: str, receipt) -> None:
        self.check_transaction(self.web3.eth.get_transaction(transaction_hash), subject)
        if hex_value(self.web3.eth.get_block(receipt["blockNumber"])["hash"]) != hex_value(receipt["blockHash"]):
            raise ChainStale
        if not any(
            event["address"].lower() == self.address.lower()
            and event["args"]["certificateId"] == subject.certificate_id
            and event["args"]["snakeId"] == subject.snake_id
            and event["args"]["issuer"].lower() == subject.issuer_address.lower()
            and event["args"]["version"] == 1 and bytes(event["args"]["fileHash"]) == subject.file_hash
            for event in self.contract.events.CertificateIssued().process_receipt(receipt)
        ):
            raise ChainConflict
        record = self.record(subject.certificate_id)
        if record is None:
            raise ChainStale
        self.assert_record(subject, record)


def get_certificate_chain() -> CertificateChain:
    return CertificateChain()
