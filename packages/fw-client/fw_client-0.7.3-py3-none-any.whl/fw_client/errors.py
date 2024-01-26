"""Flywheel client errors."""
# proxy all exceptions when accessed through the module
# then explicitly import the classes that are used directly
from fw_http_client.errors import *  # noqa: F403
from fw_http_client.errors import ClientError, Conflict, NotFound, ServerError
from requests.exceptions import *  # noqa: F403
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout

# define a limited set of explicitly exported errors
__all__ = [
    "ClientError",
    "Conflict",
    "ConnectionError",
    "HTTPError",
    "NotFound",
    "ServerError",
    "RequestException",
    "Timeout",
]
