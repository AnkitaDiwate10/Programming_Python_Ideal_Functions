import numpy as np


class IdealFunctionSelector:
    """
    This class selects the best ideal functions
    based on the least squares criterion.
    """

    def calculate_sse(self, y_train, y_ideal):
        """
        Calculate Sum of Squared Errors.
        """
        return np.sum((y_train - y_ideal) ** 2)

    def find_best_function(self, train_series, ideal_df):
        """
        Find the ideal function with the smallest error.
        """

        best_function = None
        lowest_error = float("inf")

        for column in ideal_df.columns[1:]:

            error = self.calculate_sse(train_series, ideal_df[column])

            if error < lowest_error:
                lowest_error = error
                best_function = column

        return best_function, lowest_error