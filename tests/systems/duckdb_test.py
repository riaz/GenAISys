import pytest
import logging 
from genaisys.systems.duckdb import DuckDB

@pytest.fixture(autouse=True)
def setup_logging(caplog):
    caplog.set_level(logging.INFO)

def test_duckdb(caplog):

    # Note: here use use the database connection as a context manager
    with DuckDB() as db:

        create_table = """
            CREATE TABLE users (
                id INTEGER,
                name VARCHAR,
                age INTEGER
            )
        """

        db.create_table(create_table)

        # Next we will attempt to enter 3 rows to the table
        db.add_row("INSERT INTO users VALUES (1, 'Alice', 30)")
        db.add_row("INSERT INTO users VALUES (2, 'Bob', 25)")
        db.add_row("INSERT INTO users VALUES (3, 'Charlie', 35)")

        # Getting all ther users above age 25
        result = db.query("SELECT * FROM users WHERE age > 28")    
        expected = [(1, 'Alice', 30), (3, 'Charlie', 35)]
        got = result.fetchall()

        assert got == expected

        # Getting names of the users starting with Q
        result = db.query("SELECT name FROM users WHERE name LIKE 'Q%'")
        expected = []
        got = result.fetchall()

        assert got == expected

        # Getting names of the users starting with A
        result = db.query("SELECT name FROM users WHERE name LIKE 'A%'")
        expected = [("Alice",)]
        got = result.fetchall()

        assert got == expected


        # returning a pandas dataframe
        df = db.query_to_pd("SELECT * FROM users")
        assert len(df) == 3 

        #db.__exit__() # this should get called automatically


    


