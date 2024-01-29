from pep249 import *
from larkbasedb.core import *


__version__ = "0.0.1"


# pylint: disable=invalid-name
apilevel = "2.0"
threadsafety = 1
paramstyle = "qmark"


def connect(connection_string: str = "", read_only=False) -> Connection:
    """Connect to a Lark Base, returning a connection."""
    return Connection(connection_string, read_only=read_only)

