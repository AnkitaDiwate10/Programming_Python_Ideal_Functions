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