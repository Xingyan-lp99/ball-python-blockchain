import hashlib
import os
from pathlib import Path
from uuid import uuid4

from blockchain.transactions import TransactionProblem

MAX_PDF_BYTES = 10 * 1024 * 1024


def read_pdf(upload) -> bytes:
    content = upload.file.read(MAX_PDF_BYTES + 1)
    if len(content) > MAX_PDF_BYTES:
        raise TransactionProblem(413, "PDF exceeds the 10 MiB upload limit")
    if not content.startswith(b"%PDF-") or b"%%EOF" not in content[-1024:]:
        raise TransactionProblem(422, "A PDF file with a PDF header and EOF marker is required")
    return content


def storage_root() -> Path:
    default = Path(__file__).resolve().parents[2] / ".local/certificate-files"
    return Path(os.getenv("CERTIFICATE_STORAGE_DIR", str(default))).resolve()


def save_original(content: bytes) -> tuple[str, bytes]:
    root = storage_root()
    root.mkdir(parents=True, exist_ok=True)
    key = uuid4().hex + ".pdf"
    with (root / key).open("xb") as target:
        target.write(content)
        target.flush()
        os.fsync(target.fileno())
    return key, hashlib.sha256(content).digest()


def original_path(key: str) -> Path:
    # Storage keys are internal UUIDs, never user filenames or path parameters.
    if len(key) != 36 or not key.endswith(".pdf"):
        raise TransactionProblem(503, "Stored document reference is invalid")
    try:
        int(key[:-4], 16)
    except ValueError:
        raise TransactionProblem(503, "Stored document reference is invalid") from None
    return storage_root() / key
