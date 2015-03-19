from contextlib import contextmanager

import sqlite3

DB_FILENAME = 'DB.sqlite'

__connection = None


@contextmanager
def connect():
    global __connection

    __connection = sqlite3.connect(DB_FILENAME)
    yield
    __connection.commit()
    __connection.close()


def cursor():
    if not __connection:
        return None

    return __connection.cursor()
