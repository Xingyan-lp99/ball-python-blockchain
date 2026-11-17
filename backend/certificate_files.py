import hashlib
from pathlib import Path
from uuid import uuid4


MAX_PDF_BYTES = 10 * 1024 * 1024
STORAGE_DIRECTORY = Path(__file__).resolve().parents[1] / "storage"


# Purpose: reject empty, oversized, or clearly non-PDF uploads.
# Without this check, the report archive could accept unsuitable input.
def validate_certificate_pdf(content: bytes) -> None:
    if not content:
        raise ValueError("Please upload a PDF file.")

    if len(content) > MAX_PDF_BYTES:
        raise ValueError("The PDF must not exceed 10 MB.")

    if not content.startswith(b"%PDF-"):
        raise ValueError("The uploaded file must have a PDF file header.")


# Purpose: preserve original report bytes and calculate their SHA-256.
# Without this operation, later verification would have no original file
# or reliable digest to compare with the on-chain evidence.
def save_certificate_pdf(content: bytes) -> tuple[str, str]:
    validate_certificate_pdf(content)

    reference = Path("certificates") / f"{uuid4().hex}.pdf"
    destination = STORAGE_DIRECTORY / reference
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("xb") as report:
        report.write(content)

    return reference.as_posix(), hashlib.sha256(content).hexdigest()


# Purpose: locate a preserved PDF only inside the certificate storage directory.
# Without this boundary, a stored reference could expose an unrelated local file.
def get_certificate_pdf_path(reference: str) -> Path | None:
    directory = (STORAGE_DIRECTORY / "certificates").resolve()
    path = (STORAGE_DIRECTORY / reference).resolve()

    if (
        not path.is_relative_to(directory)
        or path.suffix.lower() != ".pdf"
        or not path.is_file()
    ):
        return None

    return path
