"""Save local database/uploads/chain checkpoints without displaying credentials."""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import requests

from backend.demo_chain import ROOT, STATE_DIRECTORY, client_for, save_chain


def save_demo_backup() -> Path:
    try:
        requests.get("http://127.0.0.1:8001/health", timeout=2)
    except requests.ConnectionError:
        pass
    except requests.RequestException:
        raise RuntimeError("Backend state is uncertain; stop it before making a coordinated backup.") from None
    else:
        raise RuntimeError("Stop FastAPI before backup so uploads and database writes cannot race the checkpoint.")
    client = client_for(8545)
    if not client.is_connected():
        raise RuntimeError("The persistent local node must be running before backup.")
    head = client.eth.get_block("latest").hash.hex()
    checkpoint = save_chain(8545, STATE_DIRECTORY)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    destination = ROOT / "storage/backups" / stamp
    destination.mkdir(parents=True, exist_ok=False)
    container = "ball-python-demo-db-1"
    with (destination / "postgres.dump").open("xb") as dump:
        result = subprocess.run(
            ["docker", "exec", container, "pg_dump", "-U", "ballpython", "-d", "ballpython_demo", "-Fc"],
            stdout=dump, stderr=subprocess.PIPE,
        )
    if result.returncode:
        raise RuntimeError("Database backup failed. Incomplete backup retained for inspection; no data was deleted.")
    shutil.copy2(checkpoint, destination / "chain.json")
    for name in ("photos", "certificates"):
        source = ROOT / "storage" / name
        if source.is_dir():
            shutil.copytree(source, destination / name)
    if client.eth.get_block("latest").hash.hex() != head:
        raise RuntimeError("The chain changed during backup. This backup is incomplete; no completion manifest was written.")
    manifest = {
        "created_at_utc": stamp, "chain_id": client.eth.chain_id,
        "block_number": client.eth.block_number, "block_hash": head,
        "contracts": {key: os.environ.get(key, "") for key in (
            "DEMO_REGISTRY_ADDRESS", "DEMO_CERTIFICATE_REGISTRY_ADDRESS", "DEMO_KEEPER_TRANSFERS_ADDRESS")},
        "old_chain_evidence_restored": False,
        "note": "Complete file backup of current state; this does not recreate evidence lost before persistence was enabled.",
    }
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return destination


if __name__ == "__main__":
    try:
        print(f"Local backup saved: {save_demo_backup()}")
    except (OSError, ValueError, RuntimeError) as error:
        raise SystemExit(str(error)) from None
