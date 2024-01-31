"""Tests for db config module"""
from os import path, getcwd
from roche_datachapter_lib.db_config import DB_CONFIG
from roche_datachapter_lib.query_manager import QueryManager

print("QUERIES DIR: ",path.join(getcwd(), 'queries'))
QUERY_MANAGER = QueryManager(path.join(getcwd(), 'queries'))

for bind in DB_CONFIG.SQLALCHEMY_BINDS:
    print(f"Testing bind '{bind}'")
    RESULT = DB_CONFIG.test_bind_connection(bind)
    print(f"Bind '{bind}' test finished {'OK' if RESULT else 'with ERROR'}")
