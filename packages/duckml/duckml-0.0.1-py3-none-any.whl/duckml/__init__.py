import duckdb
from duckml.say_quack import say_quack


def load_duckml(conn: duckdb.DuckDBPyConnection):
    conn.create_function("say_quack", say_quack, [], duckdb.typing.VARCHAR)

    return conn
