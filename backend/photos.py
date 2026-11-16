from io import BytesIO
from pathlib import Path
from uuid import uuid4

from PIL import Image, UnidentifiedImageError


MAX_PHOTO_BYTES = 5 * 1024 * 1024
STORAGE_DIRECTORY = Path(__file__).resolve().parents[1] / "storage"


# Purpose: validate and store a profile photo off-chain.
# Workflow: demo step 1, registration photo upload.
# Without this function, the required photo has no saved file reference.
def save_snake_photo(content: bytes) -> str:
    if not content or len(content) > MAX_PHOTO_BYTES:
        raise ValueError("Photo must be nonempty and no larger than 5 MiB.")

    try:
        with Image.open(BytesIO(content)) as image:
            image_format = image.format
            image.verify()
    except (
        UnidentifiedImageError,
        OSError,
        SyntaxError,
        Image.DecompressionBombError,
    ):
        raise ValueError("Photo is not a readable image.") from None

    extensions = {"JPEG": "jpg", "PNG": "png"}

    if image_format not in extensions:
        raise ValueError("Only JPEG and PNG photos are supported.")

    reference = f"photos/{uuid4().hex}.{extensions[image_format]}"
    destination = STORAGE_DIRECTORY / reference
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("xb") as photo_file:
        photo_file.write(content)

    return reference

# Purpose: resolve a stored reference to an existing profile photo.
# Workflow: demo step 1, reading the saved photo.
# Without this helper, the photo endpoint cannot locate the saved image safely.
def get_snake_photo_path(reference: str) -> Path | None:
    directory = (STORAGE_DIRECTORY / "photos").resolve()
    photo_path = (STORAGE_DIRECTORY / reference).resolve()

    if (
        not photo_path.is_relative_to(directory)
        or photo_path.suffix.lower() not in {".jpg", ".png"}
        or not photo_path.is_file()
    ):
        return None

    return photo_path