from sqlalchemy import create_engine
import pandas as pd


class DatabaseManager:
    """
    Handles database creation and storing data into tables.
    """

    def __init__(self, db_name="functions.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")

    def save_training_data(self, dataframe):
        dataframe.to_sql(
            "training_data",
            self.engine,
            if_exists="replace",
            index=False
        )

    def save_ideal_functions(self, dataframe):
        dataframe.to_sql(
            "ideal_functions",
            self.engine,
            if_exists="replace",
            index=False
        )

    def save_test_results(self, dataframe):
        dataframe.to_sql(
            "test_results",
            self.engine,
            if_exists="replace",
            index=False
        )