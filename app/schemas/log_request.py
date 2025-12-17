from pydantic import BaseModel
from typing import Optional

class LogRequest(BaseModel):
    error: str

class LogResponse(BaseModel):
    uploaded_files: int
    status: str