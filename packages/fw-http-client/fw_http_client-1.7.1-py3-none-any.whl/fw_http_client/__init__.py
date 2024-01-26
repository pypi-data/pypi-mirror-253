"""Prod-ready HTTP client with timeouts and retries by default."""
from importlib.metadata import version

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    InvalidJSONError,  # type: ignore
    RequestException,
)

from . import errors
from .client import HttpClient, dump_useragent, load_useragent
from .config import AnyAuth, HttpConfig
from .errors import ClientError, Conflict, NotFound, ServerError

__version__ = version(__name__)
__all__ = [
    "AnyAuth",
    "HttpClient",
    "HttpConfig",
    "dump_useragent",
    "load_useragent",
    "errors",
    "Conflict",
    "ConnectionError",
    "ClientError",
    "NotFound",
    "RequestException",
    "ServerError",
]

# patch the exceptions for more useful default error messages
setattr(RequestException, "__getattr__", errors.request_exception_getattr)
setattr(RequestException, "__str__", errors.request_exception_str)
setattr(ConnectionError, "__str__", errors.connection_error_str)
setattr(HTTPError, "__str__", errors.http_error_str)
setattr(InvalidJSONError, "__str__", errors.json_error_str)
