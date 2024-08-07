from lib.high_value import *

"""
Return first value higher when value_first > value_second
"""
def test_first_value_higher():
    high_value = HighValue(20, 4)
    result = high_value.get_highest()
    assert result == "First value is higher"

"""
Return second value higher when value_second > value_first
"""
def test_second_value_higher():
    high_value = HighValue(4, 20)
    result = high_value.get_highest()
    assert result == "Second value is higher"

"""
Return values equal when value_first = value_second
"""
def test_first_value_equals_second_value():
    high_value = HighValue(20, 20)
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_add_to_first_and_become_higher():
    high_value = HighValue(4, 4)
    high_value.add(1, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"
