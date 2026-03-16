import numpy as np

class TestMapper:
    """
    Handles the assignment of test data points
    to the selected ideal functions.
    """
    def calculate_deviation(self, y_test, y_ideal):
        """
        Calculate absolute deviation between test value
        and ideal function value.
        """
        return abs(y_test - y_ideal)
    def map_test_point(self, y_test, y_ideal, max_deviation):

        deviation = self.calculate_deviation(y_test, y_ideal)

        if deviation <= np.sqrt(2) * max_deviation:
            return deviation
        else:
            return None