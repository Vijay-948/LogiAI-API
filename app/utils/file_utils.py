from pathlib import Path
import uuid

def save_uploaded_file(content: bytes, dest_folder: str, original_filename: str = None) -> str :
    Path(dest_folder).mkdir(parents=True, exist_ok=True)
    fname = original_filename or f"{uuid.uuid4().hex}.log"
    path = Path(dest_folder) / fname
    path.write_bytes(content)
    return str(path)