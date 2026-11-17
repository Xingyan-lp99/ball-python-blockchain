import json
import os
from pathlib import Path

import psycopg
from hexbytes import HexBytes
from requests.exceptions import RequestException
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import Web3Exception
from web3.types import TxReceipt


CERTIFICATE_ARTIFACT_PATH = (
    Path(__file__).resolve().parents[1]
    / "contracts"
    / "artifacts"
    / "contracts"
    / "CertificateRegistry.sol"
    / "CertificateRegistry.json"
)


def _wait_for_success(
    client: Web3,
    transaction_hash: HexBytes,
) -> TxReceipt:
    try:
        receipt = client.eth.wait_for_transaction_receipt(
            transaction_hash,
            timeout=30,
        )
    except (RequestException, Web3Exception):
        raise RuntimeError(
            "Transaction confirmation is unavailable. "
            f"Check {transaction_hash.to_0x_hex()} before submitting again."
        ) from None

    if receipt["status"] != 1:
        raise RuntimeError(
            f"Transaction failed: {transaction_hash.to_0x_hex()}"
        )

    return receipt


# Purpose: connect laboratory profiles to the existing local participants.
# Without these profiles, certificate series cannot reference their issuer.
def _initialize_laboratories(
    *,
    password: str,
    laboratories: list[tuple[str, str]],
) -> None:
    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
        connect_timeout=5,
    ) as connection:
        for laboratory_id, expected_address in laboratories:
            participant = connection.execute(
                """
                SELECT wallet_address
                FROM public.participants
                WHERE participant_id = %s
                """,
                (laboratory_id,),
            ).fetchone()

            if (
                participant is None
                or participant[0].lower() != expected_address.lower()
            ):
                raise RuntimeError(
                    f"Participant address does not match {laboratory_id}."
                )

            connection.execute(
                """
                INSERT INTO public.laboratories (
                    laboratory_id, participant_id, name
                )
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
                """,
                (laboratory_id, laboratory_id, laboratory_id),
            )

            stored = connection.execute(
                """
                SELECT participant_id
                FROM public.laboratories
                WHERE laboratory_id = %s
                """,
                (laboratory_id,),
            ).fetchone()

            if stored is None or stored[0] != laboratory_id:
                raise RuntimeError(
                    f"Existing laboratory profile conflicts with {laboratory_id}."
                )

    print("Laboratory profiles initialized.")


def _validate_certificate_registry(
    client: Web3,
    registry: Contract,
    *,
    snake_registry_address: str,
    administrator: str,
) -> None:
    if not client.eth.get_code(registry.address):
        raise RuntimeError("Certificate registry code is unavailable.")

    if (
        registry.functions.snakeRegistry().call().lower()
        != snake_registry_address.lower()
    ):
        raise RuntimeError(
            "Certificate registry points to a different SnakeRegistry."
        )

    if (
        registry.functions.administrator().call().lower()
        != administrator.lower()
    ):
        raise RuntimeError(
            "Certificate administrator is not local account 0."
        )


# Purpose: prepare certificate profiles, deployment, and issuance permissions.
# Workflow: laboratory setup before report upload and issuance.
# Without this setup, laboratory accounts have no usable certificate registry.
def setup_certificates(
    *,
    password: str,
    snake_registry_address: str,
    certificate_registry_address: str | None = None,
) -> str:
    client = Web3(
        Web3.HTTPProvider(
            "http://127.0.0.1:8545",
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )

    if not client.is_connected():
        raise RuntimeError("Cannot connect to the local blockchain.")

    if client.eth.chain_id != 31337:
        raise RuntimeError("Expected local chain ID 31337.")

    accounts = [str(address) for address in client.eth.accounts]

    if len(accounts) < 5:
        raise RuntimeError("At least five local accounts are required.")

    administrator = accounts[0]
    snake_address = Web3.to_checksum_address(snake_registry_address)

    if not client.eth.get_code(snake_address):
        raise RuntimeError("The existing SnakeRegistry code is unavailable.")

    artifact = json.loads(
        CERTIFICATE_ARTIFACT_PATH.read_text(encoding="utf-8")
    )

    laboratories = [
        ("LAB001", accounts[2]),
        ("LAB002", accounts[3]),
    ]

    registry = None

    if certificate_registry_address:
        registry = client.eth.contract(
            address=Web3.to_checksum_address(
                certificate_registry_address
            ),
            abi=artifact["abi"],
        )
        _validate_certificate_registry(
            client,
            registry,
            snake_registry_address=snake_address,
            administrator=administrator,
        )

    _initialize_laboratories(
        password=password,
        laboratories=laboratories,
    )

    if registry is None:
        factory = client.eth.contract(
            abi=artifact["abi"],
            bytecode=artifact["bytecode"],
        )
        transaction_hash = factory.constructor(snake_address).transact(
            {"from": administrator}
        )
        print(
            "Deployment transaction:",
            transaction_hash.to_0x_hex(),
            flush=True,
        )

        receipt = _wait_for_success(client, transaction_hash)
        address = receipt["contractAddress"]

        if not address:
            raise RuntimeError(
                "Deployment receipt contains no contract address."
            )

        registry = client.eth.contract(
            address=address,
            abi=artifact["abi"],
        )

    print("Certificate registry address:", registry.address, flush=True)
    print(
        f'$env:DEMO_CERTIFICATE_REGISTRY_ADDRESS = "{registry.address}"',
        flush=True,
    )

    _validate_certificate_registry(
        client,
        registry,
        snake_registry_address=snake_address,
        administrator=administrator,
    )

    for laboratory_id, laboratory_address in laboratories:
        if registry.functions.isAuthorizedLaboratory(
            laboratory_address
        ).call():
            print(f"{laboratory_id}: already authorized.")
            continue

        transaction_hash = registry.functions.authorizeLaboratory(
            laboratory_address
        ).transact({"from": administrator})

        print(
            f"{laboratory_id} authorization transaction:",
            transaction_hash.to_0x_hex(),
            flush=True,
        )
        _wait_for_success(client, transaction_hash)

        if not registry.functions.isAuthorizedLaboratory(
            laboratory_address
        ).call():
            raise RuntimeError(
                f"Authorization could not be verified for {laboratory_id}."
            )

        print(f"{laboratory_id}: authorized.")

    print("Certificate setup completed successfully.")
    return str(registry.address)


if __name__ == "__main__":
    password = os.environ.get("DEMO_DB_PASSWORD")
    snake_address = os.environ.get("DEMO_REGISTRY_ADDRESS")

    if not password or not snake_address:
        raise SystemExit(
            "Set DEMO_DB_PASSWORD and DEMO_REGISTRY_ADDRESS "
            "in this terminal before running setup."
        )

    try:
        setup_certificates(
            password=password,
            snake_registry_address=snake_address,
            certificate_registry_address=(
                os.environ.get("DEMO_CERTIFICATE_REGISTRY_ADDRESS") or None
            ),
        )
    except psycopg.Error:
        raise SystemExit(
            "Database initialization failed. Check the database connection "
            "and confirm migration 006 was applied."
        ) from None
    except (RequestException, Web3Exception):
        raise SystemExit(
            "A blockchain request failed. Check any printed transaction "
            "hashes before running setup again."
        ) from None
    except (RuntimeError, ValueError, OSError) as error:
        raise SystemExit(str(error)) from None
