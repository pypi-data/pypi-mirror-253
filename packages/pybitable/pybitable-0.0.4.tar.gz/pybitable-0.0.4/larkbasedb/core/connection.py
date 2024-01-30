import pep249
from pep249 import *
from .cursor import Cursor


# pylint: disable=too-many-ancestors

class Connection(pep249.Connection):

    def __init__(self, connection_string, *, read_only = None):
        self._connection = connection_string

    def commit(self):
        self._connection.commit()

    def close(self):
         pass

    def cursor(self) -> Cursor:
        return Cursor(self)

