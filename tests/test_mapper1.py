import pytest
from src.test_mapper import TestMapper


def test_calculate_deviation():
    """
    Test if deviation calculation works correctly.
    """

    mapper = TestMapper()

    result = mapper.calculate_deviation(10, 8)

    assert result == 2

def test_zero_deviation():

    mapper = TestMapper()

    result = mapper.calculate_deviation(5, 5)

    assert result == 0

def test_best_function_selection():
    """
    Test if the IdealFunctionSelector returns a valid function name.
    """
    from src.ideal_function_selector import IdealFunctionSelector
    import pandas as pd

    selector = IdealFunctionSelector()
    train_col = pd.Series([1, 2, 3])
    ideal_data = pd.DataFrame({
        "y1": [1, 2, 3],
        "y2": [3, 2, 1]
    })
    best_func, error = selector.find_best_function(train_col, ideal_data)
    assert best_func in ideal_data.columns

def test_mapping_threshold():
    """
    Test if TestMapper identifies a point within threshold as assignable.
    """
    from src.test_mapper import TestMapper
    mapper = TestMapper()
    deviation = mapper.calculate_deviation(10, 8)
    threshold = 3
    assert (deviation <= threshold) == True  # within threshold