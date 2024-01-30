import weakref
import pep249
from pep249 import *


class Cursor(pep249.CursorConnectionMixin, pep249.IterableCursorMixin, pep249.TransactionalCursor):

    def __init__(self, connection):
        self._connection = weakref.proxy(connection)

    @property
    def _closed(self):
        return self._connection._closed

    @property
    def connection(self):
        return self._connection

    @property
    def description(self):
        return None

    @property
    def rowcount(self):
        return -1

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass

    def callproc(self, procname, parameters):
        raise NotImplementedError()

    def nextset(self):
        raise NotImplementedError()

    def setinputsizes(self):
        pass

    def execute(self, operation, parameters = None):
        # pass
        return self

    def executescript(self, script):
        return self.execute(script)

    def executemany(self, operation, seq_of_parameters):
        # pass
        return self

    def fetchone(self):
        return None

    def fetchmany(self, size = None):
        return []

    def fetchall(self):
        return []

