import duckdb
import logging
import pandas as pd

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


"""
Note: Here we wil use DuckDB connection as a context manager to better manage the resources
"""

class DuckDB:
    def __enter__(self):
        # we have option of a in-memory db or a file-
        self.con = duckdb.connect(database=":memory:")
        self.logger = logger
        return self

    def create_table(self, expr):
        try:
            self.con.execute(expr)
        except Exception as e:
            self.logger.error("Connection not established with duckdb")
        self.logger.info("Created table")

    def add_row(self, row):
        try:
            self.con.execute(row)
        except Exception as e:
            self.logger.error("Unable to add row to the table")
        self.logger.info("Row was added successfully")
        
    def query(self, query_str):
        try:            
            result = self.con.execute(query_str)
        except Exception as e:
            self.logger.error(f"Unable to resolve the query {query_str}")

        return result

    def query_to_pd(self, query_str):
        try:
            df = self.con.execute(query_str).df()
        except Exception as e:
            self.logger.error(f"Unable to resolve the query {query_str}")

        return df

    def __exit__(self, exc_type, exc_val, exc_tb):
        # we need to safely close the connection
        try:
            self.con.close()
        except Exception as e:
            self.logger.Error("Unable to close connection to the database")
