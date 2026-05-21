from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class LogEntry:
    timestamp: Optional[datetime]
    ip: Optional[str]
    method: Optional[str]
    path: Optional[str]
    status: Optional[int]
    response_ms: Optional[float]
    raw: str