"""Read-only startup checks for the existing local demonstration services."""

import json
import os
from pathlib import Path

from web3 import Web3

from backend.database import check_database_connection


def check_demo_readiness() -> list[str]:
    errors = []
    password = os.environ.get("DEMO_DB_PASSWORD")
    if not password:
        errors.append("Database credential is not loaded; use --env-file .env.")
    else:
        try:
            check_database_connection(
                host="127.0.0.1", port=5433, dbname="ballpython_demo",
                user="ballpython", password=password,
            )
        except RuntimeError:
            errors.append("The demonstration database is unavailable.")

    client = Web3(Web3.HTTPProvider(
        "http://127.0.0.1:8545", request_kwargs={"timeout": 5},
        exception_retry_configuration=None,
    ))
    try:
        if not client.is_connected():
            return errors + ["The local Ethereum node is unavailable on 127.0.0.1:8545."]
        if client.eth.chain_id != 31337:
            return errors + ["Wrong blockchain: expected local chain ID 31337."]
        if client.eth.block_number == 0:
            errors.append(
                "The local chain is at block 0. Previous deployments are not present. "
                "Retained database records do not restore the old chain."
            )

        deployed = {}
        for variable, name in (
            ("DEMO_REGISTRY_ADDRESS", "SnakeRegistry"),
            ("DEMO_CERTIFICATE_REGISTRY_ADDRESS", "CertificateRegistry"),
            ("DEMO_KEEPER_TRANSFERS_ADDRESS", "KeeperTransfers"),
        ):
            address = os.environ.get(variable, "").strip()
            if not Web3.is_address(address):
                errors.append(f"{name}: {variable} is missing or invalid.")
            elif not client.eth.get_code(Web3.to_checksum_address(address)):
                errors.append(f"{name}: no deployed code exists at the configured address.")
            else:
                deployed[name] = Web3.to_checksum_address(address)

        root = Path(__file__).resolve().parents[1] / "contracts/artifacts/contracts"
        for name in ("CertificateRegistry", "KeeperTransfers"):
            if name not in deployed or "SnakeRegistry" not in deployed:
                continue
            artifact = json.loads((root / f"{name}.sol" / f"{name}.json").read_text(encoding="utf-8"))
            contract = client.eth.contract(address=deployed[name], abi=artifact["abi"])
            if contract.functions.snakeRegistry().call().lower() != deployed["SnakeRegistry"].lower():
                errors.append(f"{name}: it references a different SnakeRegistry.")
            if name == "CertificateRegistry":
                accounts = client.eth.accounts
                if len(accounts) < 5:
                    errors.append("The local chain has fewer than five demonstration accounts.")
                else:
                    for lab, address in (("LAB001", accounts[2]), ("LAB002", accounts[3])):
                        if not contract.functions.isAuthorizedLaboratory(address).call():
                            errors.append(f"{lab}: certificate issuance permission is missing.")
    except (OSError, ValueError, RuntimeError):
        errors.append("Contract validation could not complete; no write was attempted.")
    except Exception:
        # Provider failures must not print environment values or connection details.
        errors.append("Blockchain or contract validation failed; no write was attempted.")
    return errors


def main() -> int:
    errors = check_demo_readiness()
    if errors:
        print("Demo startup checks failed:")
        for error in errors:
            print(f"- {error}")
        print("Existing records were preserved. Do not reset data or replay old evidence automatically.")
        return 1
    print("Demo startup checks passed: database, chain, three contracts, registry references, and laboratory permissions.")
    print("Historical evidence and individual snake ownership still require their own on-chain checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
