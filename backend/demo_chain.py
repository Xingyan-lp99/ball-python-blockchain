"""Persistent local Anvil node; Hardhat remains the contract compiler/test runner."""

import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import time
from urllib.request import urlopen
import zipfile

from web3 import Web3


ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.10.0"
BINARY = ROOT / "storage/tools" / f"anvil-{VERSION}" / "anvil.exe"
STATE_DIRECTORY = ROOT / "storage/chain"


def install_anvil() -> Path:
    if BINARY.is_file():
        return BINARY
    if os.name != "nt":
        raise RuntimeError("Install Anvil and supply --binary on non-Windows systems.")
    base = f"https://github.com/foundry-rs/foundry/releases/download/{VERSION}/foundry_{VERSION}_win32_amd64"
    with urlopen(base + ".zip", timeout=120) as response:
        archive = response.read()
    with urlopen(base + ".sha256", timeout=30) as response:
        expected = response.read().decode().split()[0]
    if hashlib.sha256(archive).hexdigest() != expected:
        raise RuntimeError("Official Anvil archive checksum does not match.")
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        name = next(name for name in bundle.namelist() if Path(name).name == "anvil.exe")
        BINARY.parent.mkdir(parents=True, exist_ok=True)
        with BINARY.open("xb") as target:
            target.write(bundle.read(name))
    return BINARY


def client_for(port: int) -> Web3:
    return Web3(Web3.HTTPProvider(
        f"http://127.0.0.1:{port}", request_kwargs={"timeout": 10},
        exception_retry_configuration=None,
    ))


def save_chain(port: int, directory: Path) -> Path:
    client = client_for(port)
    if not client.is_connected() or client.eth.chain_id != 31337:
        raise RuntimeError("The expected local demonstration node is unavailable.")
    if "anvil" not in client.client_version.lower():
        raise RuntimeError("This node cannot export an Anvil checkpoint; it was not changed.")
    response = client.provider.make_request("anvil_dumpState", [])
    payload = response.get("result")
    if not isinstance(payload, str) or not payload.startswith("0x"):
        raise RuntimeError("The node did not return a valid state checkpoint.")
    content = bytes.fromhex(payload[2:])
    if content.startswith(b"\x1f\x8b"):
        content = gzip.decompress(content)
    json.loads(content)
    directory.mkdir(parents=True, exist_ok=True)
    temporary = directory / "checkpoint.pending"
    temporary.write_bytes(content)
    destination = directory / "checkpoint.json"
    temporary.replace(destination)
    return destination


def start_chain(port: int, directory: Path, binary: Path) -> None:
    client = client_for(port)
    if client.is_connected():
        if "anvil" in client.client_version.lower() and client.eth.chain_id == 31337 and owned_listener(port, directory):
            print(f"Persistent node already running on 127.0.0.1:{port}; existing state retained.")
            return
        # An arbitrary existing node is not proof that this state directory is active.
        raise RuntimeError(f"Port {port} already has a node. It was preserved; inspect it before starting another.")
    directory.mkdir(parents=True, exist_ok=True)
    snapshots = [p for p in (directory / "checkpoint.json", directory / "state.json") if p.exists()]
    arguments = [str(binary), "--host", "127.0.0.1", "--port", str(port),
                 "--chain-id", "31337", "--hardfork", "cancun", "--silent",
                 "--dump-state", str(directory / "state.json"),
                 "--state-interval", "2", "--preserve-historical-states"]
    if snapshots:
        snapshot = max(snapshots, key=lambda p: p.stat().st_mtime_ns)
        json.loads(snapshot.read_bytes())  # Never silently replace a damaged checkpoint with an empty chain.
        arguments += ["--load-state", str(snapshot)]
    process = subprocess.Popen(
        arguments, cwd=ROOT, stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    for _ in range(100):
        if process.poll() is not None:
            raise RuntimeError("Anvil exited during startup. Existing checkpoints were preserved.")
        if client.is_connected():
            if client.eth.chain_id != 31337 or "anvil" not in client.client_version.lower():
                process.terminate()
                raise RuntimeError("Unexpected node identity during startup.")
            (directory / "process.json").write_text(json.dumps({"pid": process.pid, "port": port}), encoding="utf-8")
            save_chain(port, directory)
            print(f"Persistent node started on 127.0.0.1:{port}; block {client.eth.block_number}.")
            print(f"State directory: {directory}")
            return
        time.sleep(0.1)
    process.terminate()
    raise RuntimeError("Anvil startup timed out; existing checkpoints were preserved.")


def owned_listener(port: int, directory: Path) -> bool:
    if os.name != "nt" or not (directory / "process.json").is_file():
        return False
    metadata = json.loads((directory / "process.json").read_text(encoding="utf-8"))
    if metadata["port"] != port:
        return False
    listeners = subprocess.check_output(["netstat", "-ano"], text=True)
    return any(
        len(fields := line.split()) >= 5 and fields[1] == f"127.0.0.1:{port}"
        and fields[-2] == "LISTENING" and fields[-1] == str(metadata["pid"])
        for line in listeners.splitlines()
    )


def stop_chain(port: int, directory: Path) -> None:
    if not owned_listener(port, directory):
        raise RuntimeError("The listening process changed; no process was stopped.")
    metadata = json.loads((directory / "process.json").read_text(encoding="utf-8"))
    save_chain(port, directory)
    os.kill(metadata["pid"], signal.SIGTERM)
    for _ in range(50):
        if not client_for(port).is_connected():
            print("Checkpoint saved; local node stopped.")
            return
        time.sleep(0.1)
    raise RuntimeError("The node is still listening; inspect it before restarting.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("start", "save", "stop"))
    parser.add_argument("--port", type=int, default=8545)
    parser.add_argument("--directory", type=Path, default=STATE_DIRECTORY)
    parser.add_argument("--binary", type=Path)
    arguments = parser.parse_args()
    try:
        if arguments.action == "start":
            start_chain(arguments.port, arguments.directory.resolve(), arguments.binary or install_anvil())
        elif arguments.action == "save":
            print(f"Checkpoint saved: {save_chain(arguments.port, arguments.directory.resolve())}")
        else:
            stop_chain(arguments.port, arguments.directory.resolve())
    except (OSError, ValueError, RuntimeError) as error:
        raise SystemExit(str(error)) from None


if __name__ == "__main__":
    main()
