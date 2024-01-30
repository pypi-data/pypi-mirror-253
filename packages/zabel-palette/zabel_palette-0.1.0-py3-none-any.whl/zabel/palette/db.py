"""DB helpers.

Seamlessly handle Oracle and Postgres databases.

Queries can use 'oracle' bindings (things like `':foo'`), even when used
on a Postgres connection.

[But obviously, if a query contain either 'oraclisms' or 'postgresisms',
it will fail when used on a non-compatible connection.]
"""

__all__ = ['get_db_connection', 'execute', 'fetchall']

import re

# import cx_Oracle as dbora
import psycopg2 as dbpg


########################################################################
# Functions

_con_typ_cache = dict()


def get_db_connection(info):
    """Return a database connection using the specified info.

    info is a ('typ', 'cnx') pair of strings. 'typ' is the database
    and is one of 'ORA', 'PG'.  'cnx' is a connection string.
    """
    db = dbora if info[0] == 'ORA' else dbpg if info[0] == 'PG' else None
    con = db.connect(info[1])
    _con_typ_cache[con] = info[0]

    return con


def _adjust_bindings(query):
    """Change Oracle bindings to PG bindings in query.

    Also escapes % characters as psycopg2 does not like them with
    bindings.
    """
    return re.sub(r':([a-z_][a-z0-9_]+)', r'%(\1)s', query.replace('%', '%%'))


def execute(con, query, **extra):
    """Return the cursor on which query was executed with extra on con.

    Thread-safe, returns a new cursor each time it is called.
    """
    _cur = con.cursor()
    if len(extra) == 0:
        _cur.execute(query)
    elif _con_typ_cache[con] == 'PG':
        _cur.execute(_adjust_bindings(query), extra)
    else:
        _cur.execute(query, extra)

    return _cur


def fetchall(con, query, **extra):
    """Return the result returned by executing query with extra on con."""
    return execute(con, query, **extra).fetchall()
