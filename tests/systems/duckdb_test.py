from genaisys.systems.duckdb import DuckDB


def test_duckdb():
    db = DuckDB()

    create_table = """
        CREATE TABLE users (
            id INTEGER,
            name VARCHAR,
            age INTEGER
        )
    """

    db.create_table(create_table)
