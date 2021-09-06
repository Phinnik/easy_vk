from ctypes import c_longdouble
from dataclasses import dataclass

from requests import Session


@dataclass
class APIOptions:
    """Dataclass for API options."""

    session: Session
    access_token: str
    v: str
    last_call_timer: c_longdouble
    delay: float
    auto_retry: bool
    max_retries: int
    timeout: int
