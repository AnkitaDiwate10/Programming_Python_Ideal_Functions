"""
data_loader.py

This module loads the datasets used in the assignment.
The datasets include training data, ideal functions, and test data.
"""

import pandas as pd


class DataLoader:
    """
    Class responsible for loading CSV files into pandas DataFrames.
    """

    def load_training_data(self, filepath):
        """
        Load training dataset.

        Parameters
        ----------
        filepath : str
            Path to training CSV file

        Returns
        -------
        pandas.DataFrame
        """
        return pd.read_csv(filepath)

    def load_ideal_functions(self, filepath):
        """
        Load ideal functions dataset.
        """
        return pd.read_csv(filepath)

    def load_test_data(self, filepath):
        """
        Load test dataset.
        """
        return pd.read_csv(filepath)