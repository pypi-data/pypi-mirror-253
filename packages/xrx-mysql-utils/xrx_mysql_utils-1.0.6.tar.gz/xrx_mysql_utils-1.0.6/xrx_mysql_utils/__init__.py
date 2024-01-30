import os
import logging
import warnings
import asyncio
from typing import Tuple, Union, List, Dict, Any

import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import MySQLConnection
from dotenv import load_dotenv
from sentry_sdk import add_breadcrumb

load_dotenv()
logg_sql = logging.getLogger("xrx_mysql_utils.sql")
logg_sql_error = logging.getLogger("xrx_mysql_utils.sql_error")

MYSQL_USER = str(os.getenv("MYSQL_USER"))
MYSQL_PASS = str(os.getenv("MYSQL_PASS"))
MYSQL_HOST = str(os.getenv("MYSQL_HOST"))
MYSQL_DB = str(os.getenv("MYSQL_DB"))


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""

    def newFunc(*args, **kwargs):
        warnings.simplefilter("always", DeprecationWarning)  # turn off filter
        warnings.warn(
            "Call to deprecated function %s." % func.__name__,
            category=DeprecationWarning,
            stacklevel=2,
        )
        warnings.simplefilter("default", DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc


def connect_to_mysql(
    user="", password="", host="", database=""
) -> MySQLConnection:  # pragma: no cover
    """Connect to the MySQL server."""
    if user:
        cnx = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
        )
    else:
        cnx = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASS,
            host=MYSQL_HOST,
            database=MYSQL_DB,
        )
    return cnx  # type: ignore


class connect_to_mysql_with_as(object):
    def __init__(self, user="", password="", host="", database="") -> None:
        if user:
            self.cnx = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database,
            )
        else:
            self.cnx = mysql.connector.connect(
                user=MYSQL_USER,
                password=MYSQL_PASS,
                host=MYSQL_HOST,
                database=MYSQL_DB,
            )

    def __enter__(self) -> MySQLConnection:
        return self.cnx  # type: ignore

    def __exit__(self, type, value, traceback):
        self.cnx.close()


def esc(string: Union[str, int, bool, float]) -> str:
    string = str(string)
    return string.translate(
        string.maketrans(
            {  # type: ignore
                "\0": "\\0",
                "\x08": "\\b",
                "\x09": "\\t",
                "\x1a": "\\z",
                "\n": "\\n",
                "\r": "\\r",
                '"': '\\"',
                "'": "\\'",
                "\\": "\\\\",
            }
        )
    )


def split_keys_values_for_mysql(dictobj: dict) -> Tuple[str, str]:
    """Split a dictonary into columns and values.

    ### Parameters:
        dictobj (dict): Dictonary with key and values
    ### Returns:
        Tuple(columns:str, values: str)
    """
    columns = ""
    for column in dictobj.keys():
        columns += f"`{esc(column)}`,"

    values = ""
    for value in dictobj.values():
        if value == "":
            values = values + "'',"
        elif value == 0:
            values = values + f"'{esc(value)}',"
        elif not value:
            values = values + "NULL,"
        else:
            values = values + f"'{esc(value)}',"

    values = values.strip(",")
    columns = columns.strip(",")

    return (columns, values)


def save_object(table: str, obj: dict) -> None:  # pragma: no cover
    """Convert a dictonary into columns/values and then insert it into a mysql table."""
    cnx = connect_to_mysql()
    (columns, values) = split_keys_values_for_mysql(obj)
    cursor = cnx.cursor()
    sql = f"INSERT INTO {esc(table)} ({columns}) VALUES ({values})"
    cursor.execute(sql)
    cnx.commit()


async def save_object_async(table: str, obj: dict) -> None:  # pragma: no cover
    await asyncio.to_thread(save_object, table, obj)


@deprecated
def create_dict_from_mysql_cursor(
    cursor: MySQLCursor, fetchone: bool = True, fetchall: bool = False
) -> Union[List[Dict[Any, Any]], Dict[Any, Any]]:
    """Create dict from Mysql cursor response."""
    list_data: List[Dict[Any, Any]]
    dict_data: Dict[Any, Any]
    desc = cursor.description
    column_names = [col[0] for col in desc]  # type: ignore
    if not fetchone and not fetchall:
        fetchall = True
    if fetchall:
        fetchone = False
        db_data = cursor.fetchall()
    else:
        db_data = cursor.fetchone()
    if db_data:
        if fetchall:
            list_data = [dict(zip(column_names, row)) for row in db_data]
            return list_data
        else:
            dict_data = dict(zip(column_names, db_data))
            return dict_data
    else:
        if fetchall:
            list_data = []
            return list_data
        else:
            dict_data = {}
            return dict_data


def mysql_cursor_fetchone(cursor: MySQLCursor) -> Dict[Any, Any]:
    """Create dict from Mysql cursor response."""
    dict_data: Dict[Any, Any]
    desc = cursor.description
    column_names = [col[0] for col in desc]  # type: ignore
    db_data = cursor.fetchone()
    if db_data:
        dict_data = dict(zip(column_names, db_data))
        return dict_data
    else:
        dict_data = {}
        return dict_data


async def mysql_cursor_fetchone_async(cursor: MySQLCursor) -> Dict[Any, Any]:
    return await asyncio.to_thread(mysql_cursor_fetchone, cursor)


def mysql_cursor_fetchall(cursor: MySQLCursor) -> List[Dict[Any, Any]]:
    """Create dict from Mysql cursor response."""
    list_data: List[Dict[Any, Any]]
    desc = cursor.description
    column_names = [col[0] for col in desc]  # type: ignore
    db_data = cursor.fetchall()
    if db_data:
        list_data = [dict(zip(column_names, row)) for row in db_data]
        return list_data
    else:
        list_data = []
        return list_data


async def mysql_cursor_fetchall_async(cursor: MySQLCursor) -> List[Dict[Any, Any]]:
    return await asyncio.to_thread(mysql_cursor_fetchall, cursor)


def mysql_execute(cnx: MySQLConnection, sql: str, logging: bool = False) -> MySQLCursor:
    cursor = cnx.cursor()
    try:
        if logging:
            logg_sql.info(sql)
        add_breadcrumb(category="sql", message=sql, level="info")
        cursor.execute(sql)
    except Exception as ex:
        # logg_sql_error.info(sql)
        add_breadcrumb(category="sql_error", message=sql, level="error")
        cnx.close()
        raise ex
    return cursor


async def mysql_execute_async(cnx: MySQLConnection, sql: str) -> MySQLCursor:
    return await asyncio.to_thread(mysql_execute, cnx, sql)
