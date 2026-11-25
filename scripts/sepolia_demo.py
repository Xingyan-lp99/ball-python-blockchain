"""Standalone Sepolia demo. Default mode performs read-only checks."""

import argparse
import getpass
import hashlib
import json
import os
import re
import sys
import time
import warnings
from pathlib import Path
from urllib.parse import urlsplit

from web3 import HTTPProvider, Web3
from web3.exceptions import TransactionNotFound


ROOT = Path(__file__).resolve().parents[1]
CHAIN_ID = 11155111
SELLER = Web3.to_checksum_address(
    "0x53c31f84Ea3F2b0A1c856a30ab519b8c8Dc55a57"
)
LABS = [
    Web3.to_checksum_address(
        "0x95D61329A586379C6fB19Ebe60F778821319d0f0"
    ),
    Web3.to_checksum_address(
        "0x2f3D117EacB4e0F5edA8c2d33eC6Ad5B59aDB6E3"
    ),
]
NAMES = ["SnakeRegistry", "CertificateRegistry", "KeeperTransfers"]
STEPS = NAMES + ["authorize_LAB001", "authorize_LAB002", "register_pet"]
# The registry cap includes headroom over the measured Sepolia deployment Gas.
# Later steps still require estimates against their deployed dependencies.
GAS_CAPS = [3_000_000, 20_000_000, 9_100_000, 200_000, 200_000, 200_000]
MAX_FEE = Web3.to_wei(1, "gwei")
MAX_TOTAL = Web3.to_wei("0.03", "ether")
RECEIPT_TIMEOUT = 180
CONFIRMATIONS = 2


class StopDemo(Exception):
    """An expected, safely reportable stop condition."""


def require(condition, message):
    if not condition:
        raise StopDemo(message)


def hex_value(value):
    return Web3.to_hex(value)


def read_rpc(path):
    require(path.is_file(), "RPC configuration file is missing.")
    entries = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, separator, value = line.partition("=")
        name = name.strip()
        require(
            separator and name == "SEPOLIA_RPC_URL" and name not in entries,
            "Use exactly one SEPOLIA_RPC_URL entry in the configuration file.",
        )
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        entries[name] = value
    url = entries.get("SEPOLIA_RPC_URL", "")
    parsed = urlsplit(url)
    require(
        parsed.scheme == "https" and parsed.hostname,
        "An HTTPS RPC URL is required.",
    )
    return url


def load_artifacts():
    artifacts = {}
    fingerprints = {}
    for name in NAMES:
        path = ROOT / f"contracts/artifacts/contracts/{name}.sol/{name}.json"
        raw = path.read_bytes()
        artifact = json.loads(raw)
        require(artifact["contractName"] == name, "Artifact name mismatch.")
        require(
            artifact["abi"] and not artifact.get("linkReferences"),
            "Invalid ABI or unresolved library references.",
        )
        require(
            artifact["bytecode"].startswith("0x")
            and len(bytes.fromhex(artifact["bytecode"][2:])) > 0,
            "Invalid deployment bytecode.",
        )

        build_id = artifact["buildInfoId"]
        require(
            re.fullmatch(r"[A-Za-z0-9_-]+", build_id),
            "Invalid build information identifier.",
        )
        build_dir = ROOT / "contracts/artifacts/build-info"
        build = json.loads((build_dir / f"{build_id}.json").read_text())
        output = json.loads(
            (build_dir / f"{build_id}.output.json").read_text()
        )
        source_name = artifact["inputSourceName"]
        source = (ROOT / f"contracts/contracts/{name}.sol").read_text()
        compiled_source = build["input"]["sources"][source_name]["content"]
        require(
            source == compiled_source.replace("\r\n", "\n"),
            "Source differs from the Artifact build input.",
        )
        compiled = output["output"]["contracts"][source_name][name]
        require(
            artifact["abi"] == compiled["abi"]
            and artifact["bytecode"][2:] == compiled["evm"]["bytecode"]["object"]
            and artifact["deployedBytecode"][2:]
            == compiled["evm"]["deployedBytecode"]["object"],
            "Artifact differs from its compiler output.",
        )
        artifact["_immutableReferences"] = compiled["evm"][
            "deployedBytecode"
        ].get("immutableReferences", {})
        artifacts[name] = artifact
        fingerprints[name] = hashlib.sha256(raw).hexdigest()
        print(
            f"Artifact {name}: OK; "
            f"creation bytecode {(len(artifact['bytecode']) - 2) // 2} bytes"
        )
    return artifacts, fingerprints


def connect(path):
    # Disabling provider retries also prevents implicit send retries.
    provider = HTTPProvider(
        read_rpc(path),
        request_kwargs={"timeout": 20},
        exception_retry_configuration=None,
    )
    web3 = Web3(provider)
    require(web3.eth.chain_id == CHAIN_ID, "Wrong Chain ID; stopped.")
    print(f"Chain ID: {CHAIN_ID}")
    print(f"Seller: {SELLER}")
    print(f"LAB001: {LABS[0]}")
    print(f"LAB002: {LABS[1]}")
    return web3


def load_state(path, identity):
    if not path.exists():
        require(
            not path.parent.exists() or not any(path.parent.iterdir()),
            "Deployment directory exists without state.json; inspect manually.",
        )
        return {"identity": identity, "base_nonce": None, "steps": []}
    state = json.loads(path.read_text(encoding="utf-8"))
    require(state.get("identity") == identity, "Checkpoint identity mismatch.")
    steps = state.get("steps")
    require(isinstance(steps, list) and len(steps) <= 6, "Invalid checkpoint.")
    for index, step in enumerate(steps):
        require(step.get("name") == STEPS[index], "Checkpoint order mismatch.")
        require(
            index == len(steps) - 1 or step.get("status") == "confirmed",
            "Checkpoint has an unresolved earlier step.",
        )
    return state


def save_state(path, state):
    # The signed transaction is never written to disk.
    temporary = path.with_suffix(".tmp")
    payload = json.dumps(state, indent=2, sort_keys=True)
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def contract(web3, artifacts, state, index):
    address = state["steps"][index]["evidence"]["contract_address"]
    return web3.eth.contract(address=address, abi=artifacts[NAMES[index]]["abi"])


def action(web3, artifacts, state, index):
    if index < 3:
        factory = web3.eth.contract(
            abi=artifacts[NAMES[index]]["abi"],
            bytecode=artifacts[NAMES[index]]["bytecode"],
        )
        if index == 0:
            return factory.constructor()
        registry = state["steps"][0]["evidence"]["contract_address"]
        return factory.constructor(registry)
    if index < 5:
        return contract(web3, artifacts, state, 1).functions.authorizeLaboratory(
            LABS[index - 3]
        )
    return contract(web3, artifacts, state, 0).functions.registerSnake(
        state["identity"]["pet_id"]
    )


def fee_quote(web3):
    require(web3.eth.chain_id == CHAIN_ID, "Chain ID changed.")
    block = web3.eth.get_block("latest")
    priority = web3.eth.max_priority_fee
    maximum = 2 * block["baseFeePerGas"] + priority
    require(0 < maximum <= MAX_FEE, "Current fee quote exceeds the fee cap.")
    return maximum, priority


def check_budget(web3, state, start):
    spent = sum(
        step.get("evidence", {}).get("fee_wei", 0)
        for step in state["steps"]
    )
    reserve = sum(GAS_CAPS[start:]) * MAX_FEE
    require(spent + reserve <= MAX_TOTAL, "Total fee budget would be exceeded.")
    require(
        web3.eth.get_balance(SELLER, "pending") >= reserve,
        "Seller balance is below the remaining conservative fee reserve.",
    )


def preflight(web3, artifacts, state):
    balance = web3.eth.get_balance(SELLER)
    print(f"Seller balance: {Web3.from_wei(balance, 'ether')} SepoliaETH")
    print(
        "Full-run conservative fee reserve: "
        f"{Web3.from_wei(sum(GAS_CAPS) * MAX_FEE, 'ether')} SepoliaETH"
    )
    latest = web3.eth.get_transaction_count(SELLER, "latest")
    pending = web3.eth.get_transaction_count(SELLER, "pending")
    require(latest == pending, "Seller has pending transactions; query first.")
    require(
        all(step["status"] == "confirmed" for step in state["steps"]),
        "An unresolved checkpoint exists; use status mode.",
    )
    index = len(state["steps"])
    if index == 6:
        print("All six steps are already recorded. No new transaction needed.")
        return

    check_budget(web3, state, index)
    maximum, priority = fee_quote(web3)
    transaction = action(web3, artifacts, state, index).build_transaction({
        "from": SELLER,
        "chainId": CHAIN_ID,
        "nonce": latest,
        "value": 0,
        "gas": GAS_CAPS[index],
        "maxFeePerGas": maximum,
        "maxPriorityFeePerGas": priority,
    })
    # Estimate without the local cap, then enforce it before any signing.
    estimate = web3.eth.estimate_gas({
        key: value for key, value in transaction.items() if key != "gas"
    })
    buffered = (estimate * 120 + 99) // 100
    require(
        buffered <= GAS_CAPS[index],
        f"Buffered Gas {buffered} exceeds step cap {GAS_CAPS[index]}.",
    )
    print(f"Next step: {STEPS[index]}")
    print(f"Estimated Gas: {estimate}; buffered Gas: {buffered}")
    print(f"Current maxFeePerGas: {Web3.from_wei(maximum, 'gwei')} Gwei")
    print("Preflight passed. Later steps require fresh estimates after deployment.")


def verify_runtime(web3, artifact, address):
    actual = bytearray(web3.eth.get_code(address))
    expected = bytearray.fromhex(artifact["deployedBytecode"][2:])
    require(actual and len(actual) == len(expected), "Runtime code mismatch.")
    # Constructor-set immutable values are checked separately through getters.
    for references in artifact["_immutableReferences"].values():
        for reference in references:
            start, length = reference["start"], reference["length"]
            actual[start:start + length] = bytes(length)
            expected[start:start + length] = bytes(length)
    require(actual == expected, "Runtime code differs from the Artifact.")


def verify_step(web3, artifacts, state, index):
    step = state["steps"][index]
    receipt = web3.eth.get_transaction_receipt(step["hash"])
    require(receipt["status"] == 1, "Transaction reverted; manual review required.")
    require(
        web3.eth.get_block(receipt["blockNumber"])["hash"] == receipt["blockHash"],
        "Receipt block is no longer canonical.",
    )
    if web3.eth.block_number < receipt["blockNumber"] + CONFIRMATIONS - 1:
        return None

    transaction = web3.eth.get_transaction(step["hash"])
    saved = step["transaction"]
    require(
        hex_value(transaction["hash"]) == step["hash"]
        and transaction["from"] == SELLER
        and transaction["nonce"] == state["base_nonce"] + index
        and transaction["chainId"] == CHAIN_ID
        and transaction["value"] == 0
        and hex_value(transaction["input"]) == saved["data"]
        and (transaction["to"] or "").lower()
        == (saved.get("to") or "").lower(),
        "Mined transaction does not match the checkpoint.",
    )

    evidence = {
        "transaction_hash": step["hash"],
        "receipt_status": receipt["status"],
        "block_number": receipt["blockNumber"],
        "block_hash": hex_value(receipt["blockHash"]),
        "gas_used": receipt["gasUsed"],
        "fee_wei": receipt["gasUsed"] * receipt["effectiveGasPrice"],
        "etherscan": f"https://sepolia.etherscan.io/tx/{step['hash']}",
    }
    if index < 3:
        address = receipt["contractAddress"]
        require(address is not None, "Deployment has no contract address.")
        verify_runtime(web3, artifacts[NAMES[index]], address)
        deployed = web3.eth.contract(
            address=address, abi=artifacts[NAMES[index]]["abi"]
        )
        if index > 0:
            expected = state["steps"][0]["evidence"]["contract_address"]
            require(
                deployed.functions.snakeRegistry().call() == expected,
                "Constructor registry dependency mismatch.",
            )
        if index == 1:
            require(
                deployed.functions.administrator().call() == SELLER,
                "Administrator mismatch.",
            )
        evidence["contract_address"] = address
    elif index < 5:
        certificates = contract(web3, artifacts, state, 1)
        lab = LABS[index - 3]
        events = certificates.events.LaboratoryAuthorized().process_receipt(
            receipt
        )
        require(
            len(events) == 1
            and events[0]["address"] == certificates.address
            and events[0]["args"]["laboratory"] == lab
            and certificates.functions.isAuthorizedLaboratory(lab).call(),
            "Laboratory authorization verification failed.",
        )
        evidence["laboratory"] = lab
    else:
        registry = contract(web3, artifacts, state, 0)
        keeper = contract(web3, artifacts, state, 2)
        pet_id = state["identity"]["pet_id"]
        events = registry.events.SnakeRegistered().process_receipt(receipt)
        require(
            len(events) == 1
            and events[0]["address"] == registry.address
            and events[0]["args"]["snakeId"] == pet_id
            and events[0]["args"]["keeper"] == SELLER
            and registry.functions.getCurrentKeeper(pet_id).call() == SELLER
            and keeper.functions.getCurrentKeeper(pet_id).call() == SELLER,
            "Pet registration or keeper verification failed.",
        )
        evidence.update(pet_id=pet_id, initial_keeper=SELLER)
    return evidence


def report_status(web3, artifacts, state):
    if not state["steps"]:
        print("No recorded transactions.")
    for index, step in enumerate(state["steps"]):
        try:
            evidence = verify_step(web3, artifacts, state, index)
        except TransactionNotFound:
            evidence = None
        print(f"{step['name']}: {step['hash']}")
        print(json.dumps(evidence, indent=2) if evidence else "Pending/unknown.")
    print("Status mode performed no broadcasts and no checkpoint writes.")


def execute(web3, artifacts, path, identity):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.parent / "execution.lock"
    try:
        lock_handle = lock.open("x", encoding="utf-8")
    except FileExistsError:
        raise StopDemo("Execution lock exists; inspect it manually.") from None

    try:
        with lock_handle:
            lock_handle.write(str(os.getpid()))
            lock_handle.flush()

        # Reload under the lock; an empty new directory now contains our lock.
        if path.exists():
            state = load_state(path, identity)
        else:
            require(
                set(path.parent.iterdir()) == {lock},
                "Unexpected deployment files exist; inspect manually.",
            )
            state = {"identity": identity, "base_nonce": None, "steps": []}

        # Reconcile existing hashes before accessing a signing key.
        for index, step in enumerate(state["steps"]):
            try:
                evidence = verify_step(web3, artifacts, state, index)
            except TransactionNotFound:
                evidence = None
            require(evidence is not None, "Existing transaction remains unresolved.")
            if step["status"] != "confirmed":
                step.update(status="confirmed", evidence=evidence)
                save_state(path, state)
                print("Existing transaction reconciled. Stopped without broadcasting.")
                return
            require(
                step["evidence"] == evidence,
                "Previously confirmed evidence changed; inspect manually.",
            )

        preflight(web3, artifacts, state)
        if len(state["steps"]) == 6:
            return

        require(sys.stdin.isatty(), "Execution requires an interactive terminal.")
        with warnings.catch_warnings():
            warnings.simplefilter("error", getpass.GetPassWarning)
            account = web3.eth.account.from_key(
                getpass.getpass("Seller private key (hidden, memory only): ")
            )
        require(account.address == SELLER, "Signing account is not Seller.")

        if state["base_nonce"] is None:
            state["base_nonce"] = web3.eth.get_transaction_count(SELLER, "latest")
            save_state(path, state)

        for index in range(len(state["steps"]), 6):
            expected_nonce = state["base_nonce"] + index
            require(
                web3.eth.get_transaction_count(SELLER, "latest") == expected_nonce
                == web3.eth.get_transaction_count(SELLER, "pending"),
                "Unexpected nonce or pending transaction; stopped.",
            )
            check_budget(web3, state, index)
            maximum, priority = fee_quote(web3)
            transaction = action(web3, artifacts, state, index).build_transaction({
                "from": SELLER,
                "chainId": CHAIN_ID,
                "nonce": expected_nonce,
                "value": 0,
                "gas": GAS_CAPS[index],
                "maxFeePerGas": maximum,
                "maxPriorityFeePerGas": priority,
            })
            estimate = web3.eth.estimate_gas({
                key: value for key, value in transaction.items() if key != "gas"
            })
            transaction["gas"] = (estimate * 120 + 99) // 100
            require(
                transaction["gas"] <= GAS_CAPS[index],
                f"Buffered Gas {transaction['gas']} exceeds step cap "
                f"{GAS_CAPS[index]}.",
            )

            signed = account.sign_transaction(transaction)
            # Contract creation uses an empty bytes destination in web3.py.
            # Omit it only from the JSON record; leave the signed transaction intact.
            checkpoint_transaction = dict(transaction)
            if not checkpoint_transaction.get("to"):
                checkpoint_transaction.pop("to", None)
            step = {
                "name": STEPS[index],
                "status": "prepared",
                "hash": hex_value(signed.hash),
                "transaction": checkpoint_transaction,
            }
            state["steps"].append(step)

            # A failed save raises before the only broadcast call.
            save_state(path, state)

            # Recheck immediately before broadcasting. Failure leaves a known hash.
            require(web3.eth.chain_id == CHAIN_ID, "Chain ID changed.")
            require(
                web3.eth.get_transaction_count(SELLER, "latest") == expected_nonce
                == web3.eth.get_transaction_count(SELLER, "pending"),
                "Nonce changed before broadcast.",
            )
            check_budget(web3, state, index)
            block = web3.eth.get_block("latest")
            require(
                block["baseFeePerGas"] + priority <= maximum <= MAX_FEE,
                "Fees changed before broadcast.",
            )

            try:
                returned = web3.eth.send_raw_transaction(signed.raw_transaction)
                require(
                    hex_value(returned) == step["hash"],
                    "Broadcast returned an unexpected transaction hash.",
                )
                step["status"] = "pending"
                save_state(path, state)
                print(f"{step['name']}: {step['hash']}")

                deadline = time.monotonic() + RECEIPT_TIMEOUT
                evidence = None
                while time.monotonic() < deadline:
                    try:
                        evidence = verify_step(web3, artifacts, state, index)
                    except TransactionNotFound:
                        evidence = None
                    if evidence:
                        break
                    time.sleep(3)
                require(evidence is not None, "Receipt confirmation timed out.")
            except Exception:
                step["status"] = "unknown"
                save_state(path, state)
                raise StopDemo(
                    "Transaction outcome requires review. "
                    "Use status mode; do not resubmit or replace the checkpoint."
                ) from None

            step.update(status="confirmed", evidence=evidence)
            save_state(path, state)
            print(json.dumps(evidence, indent=2))
        print("All six transactions verified.")
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--execute", action="store_true")
    mode.add_argument("--status", action="store_true")
    parser.add_argument("--env", type=Path, default=ROOT / ".env.sepolia")
    parser.add_argument("--deployment-id", default="sepolia-p0-001")
    parser.add_argument("--pet-id", default="SEPOLIA-PET-DOG-001")
    args = parser.parse_args()

    require(
        re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", args.deployment_id),
        "Invalid deployment ID.",
    )
    require(
        args.pet_id.strip() and len(args.pet_id.encode("utf-8")) <= 64,
        "Pet ID must be nonblank and at most 64 UTF-8 bytes.",
    )
    artifacts, fingerprints = load_artifacts()
    web3 = connect(args.env)
    identity = {
        "chain_id": CHAIN_ID,
        "genesis_hash": hex_value(web3.eth.get_block(0)["hash"]),
        "seller": SELLER,
        "laboratories": LABS,
        "pet_id": args.pet_id,
        "artifacts": fingerprints,
        "deployment_id": args.deployment_id,
    }
    path = ROOT / "storage/sepolia" / args.deployment_id / "state.json"
    state = load_state(path, identity)

    if args.status:
        report_status(web3, artifacts, state)
    elif args.execute:
        execute(web3, artifacts, path, identity)
    else:
        # Recheck recorded evidence without changing the checkpoint.
        for index, step in enumerate(state["steps"]):
            require(
                step["status"] == "confirmed",
                "Unresolved transaction exists; use status mode.",
            )
            require(
                verify_step(web3, artifacts, state, index) == step["evidence"],
                "Recorded evidence could not be reconfirmed.",
            )
        preflight(web3, artifacts, state)


if __name__ == "__main__":
    try:
        main()
    except StopDemo as error:
        print(f"STOP: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("STOP: Interrupted. Query recorded hashes before continuing.",
              file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        # RPC exception text can contain credentials; never print it.
        print(
            f"STOP: {type(error).__name__}. "
            "Details suppressed to protect credentials; no automatic retry.",
            file=sys.stderr,
        )
        sys.exit(1)
