from unittest.mock import Mock, patch

import pytest

from backend.demo_backup import save_demo_backup
from backend.demo_chain import BINARY, start_chain


def test_backup_requires_paused_backend():
    with patch("backend.demo_backup.requests.get", return_value=Mock()), patch("backend.demo_backup.subprocess.run") as command:
        with pytest.raises(RuntimeError, match="Stop FastAPI"):
            save_demo_backup()
    command.assert_not_called()


def test_damaged_checkpoint_does_not_start_empty_node(tmp_path):
    checkpoint = tmp_path / "checkpoint.json"
    checkpoint.write_text("damaged checkpoint", encoding="utf-8")
    client = Mock()
    client.is_connected.return_value = False
    with patch("backend.demo_chain.client_for", return_value=client), patch("backend.demo_chain.subprocess.Popen") as launch:
        with pytest.raises(ValueError):
            start_chain(8545, tmp_path, BINARY)
    launch.assert_not_called()
    assert checkpoint.read_text(encoding="utf-8") == "damaged checkpoint"


def test_foreign_node_is_not_overwritten(tmp_path):
    client = Mock()
    client.is_connected.return_value = True
    client.client_version = "Hardhat"
    with patch("backend.demo_chain.client_for", return_value=client), patch("backend.demo_chain.subprocess.Popen") as launch:
        with pytest.raises(RuntimeError, match="already has a node"):
            start_chain(8545, tmp_path, BINARY)
    launch.assert_not_called()
