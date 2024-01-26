"""Flywheel HTTP API Client."""
from importlib.metadata import version

from fw_http_client.errors import ClientError, Conflict, NotFound, ServerError
from requests.exceptions import ConnectionError, RequestException

from . import errors
from .client import FWClient
from .config import FWClientConfig

__version__ = version(__name__)
__all__ = [
    "FWClient",
    "FWClientConfig",
    "Conflict",
    "ConnectionError",
    "ClientError",
    "errors",
    "NotFound",
    "RequestException",
    "ServerError",
]
