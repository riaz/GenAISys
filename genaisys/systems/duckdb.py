import duckdb
import logging
import pandas as pd

logger = logging.getLogger(__name__)

class DuckDB:
    def __init__(self):
        # we have option of a in-memory db or a file-
        self.con = duckdb.connect(database=":memory:")

    def create_table(self, expr):
        try:
            self.con.execute(expr)
        except Exception as e:
            logger.error("Connection not established with duckdb")
        logger.info("Created table")



    def add_row(self, row):
        try:
            self.con.execute(row)
        except Exception as e:
            logger.error("Unable to add row to the table")
        logger.info("Row was added successfully")

    def query(self, query_str):
        try:            
            result = self.con.execute(query_str)
        except Exception as e:
            logger.error(f"Unable to resolve the query {query_str}")

        return result

    def query_to_pd(self, query_str):
        try:
            df = self.con.execute(query_str).df()
        except Exception as e:
            logger.error(f"Unable to resolve the query {query_str}")

        return df

    def __exit__(self):
        # we need to safely close the connection
        try:
            self.con.close()
        except Exception as e:
            logger.Error("Unable to close connection to the database")
