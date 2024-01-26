"""Flywheel HTTP API Client."""
from importlib.metadata import version

from fw_http_client.errors import ClientError, Conflict, NotFound, ServerError
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout

from . import errors
from .client import FWClient
from .config import FWClientConfig

__version__ = version(__name__)
__all__ = [
    "ClientError",
    "Conflict",
    "ConnectionError",
    "errors",
    "FWClient",
    "FWClientConfig",
    "HTTPError",
    "NotFound",
    "RequestException",
    "ServerError",
    "Timeout",
]
