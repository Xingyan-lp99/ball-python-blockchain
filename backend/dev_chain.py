"""Run the existing Hardhat node without writing its default private-key banner."""

import shutil
import subprocess
import time
from pathlib import Path

import requests


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    node = shutil.which("node")
    if not node:
        raise SystemExit("Node.js is not available")
    try:
        requests.post("http://127.0.0.1:8545", json={"jsonrpc": "2.0", "id": 1, "method": "eth_chainId", "params": []}, timeout=1).raise_for_status()
    except requests.RequestException:
        pass
    else:
        raise SystemExit("Port 8545 already has an RPC server; existing chain was left unchanged")
    process = subprocess.Popen(
        [node, str(root / "contracts/node_modules/hardhat/dist/src/cli.js"), "node", "--hostname", "127.0.0.1"],
        cwd=root / "contracts", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    try:
        for _ in range(100):
            if process.poll() is not None:
                raise SystemExit("Hardhat node exited before startup")
            try:
                result = requests.post("http://127.0.0.1:8545", json={"jsonrpc": "2.0", "id": 1, "method": "eth_chainId", "params": []}, timeout=1).json()
                if result.get("result") == "0x7a69":
                    print("Local Hardhat chain ready at 127.0.0.1:8545 (chain ID 31337). Private-key output suppressed.", flush=True)
                    break
            except (requests.RequestException, ValueError):
                pass
            time.sleep(0.1)
        else:
            raise SystemExit("Hardhat startup timed out")
        process.wait()
    except KeyboardInterrupt:
        pass
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=10)


if __name__ == "__main__":
    main()
