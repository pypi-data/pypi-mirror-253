# type: ignore
import pytest
import mysql


from xrx_mysql_utils import (
    split_keys_values_for_mysql,
    mysql_cursor_fetchone,
    mysql_cursor_fetchall,
    connect_to_mysql,
    mysql_execute,
)


def test_mysql_execute():
    cnx = connect_to_mysql()
    sql = "SELECT * FROM nisse WHERE 1=1"
    with pytest.raises(mysql.connector.errors.ProgrammingError):
        mysql_execute(cnx, sql)


def test_split_keys_values_for_mysql():
    dictobj = {
        "int": 1,
        "text": "Hej",
        "float": 0.0,
        "sql_injection": "' or 1=1;-",
        "null": None,
        "empty": "",
    }
    assert split_keys_values_for_mysql(dictobj) == (
        "`int`,`text`,`float`,`sql_injection`,`null`,`empty`",
        "'1','Hej','0.0','\\' or 1=1;-',NULL,''",
    )


def test_mysql_cursor_fetchall():
    class Cursor:
        description = ["a", "b"]

        def fetchone(self):
            return ("1", "2")

        def fetchall(self):
            return [("1", "2"), ("2", "2")]

    cursor = Cursor()

    assert mysql_cursor_fetchone(cursor) == {"a": "1", "b": "2"}
    assert mysql_cursor_fetchall(cursor) != {
        "a": "1",
        "b": "2",
    }
    assert mysql_cursor_fetchall(cursor) == [
        {"a": "1", "b": "2"},
        {"a": "2", "b": "2"},
    ]
    assert mysql_cursor_fetchall(cursor) == [
        {"a": "1", "b": "2"},
        {"a": "2", "b": "2"},
    ]


def test_mysql_cursor_fetchall_no_data():
    class Cursor:
        description = ["a", "b"]

        def fetchone(self):
            return None

        def fetchall(self):
            return None

    cursor = Cursor()

    assert mysql_cursor_fetchone(cursor) == {}
    assert mysql_cursor_fetchall(cursor) != {}
    assert mysql_cursor_fetchall(cursor) == []
    assert mysql_cursor_fetchall(cursor) != {}
