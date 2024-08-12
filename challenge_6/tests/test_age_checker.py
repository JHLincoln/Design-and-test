
from lib.age_checker import age_checker

"""
Date input correct, 16<, access granted
"""
def test_over_16_correct_format_input():
    result = age_checker("1980-10-25")
    assert result == "Access granted."

"""
Date input correct, 16>, "You are X, you need to be 16 to access this."
"""
def test_under_16_correct_format_input():
    result = age_checker("2020-10-25")
    assert result == "You are 3, you need to be 16 to access this."

"""
Date input correct, =16, access granted
"""
def test_equal_16_correct_format_input():
    result = age_checker("2008-05-25")
    assert result == "Access granted."

# Tests - 

# If date input in correct format, and over 16, say access is granted

# If date input in correct format, and not old enough, return "You are X, you need to be 16 to access this."

# If date input is in correct format, and equal 16, say access is granted



# Extra Chilli - 

# If no date is input, error message - "DoB input incorrectly, please use the format YYYY-MM-DD"

# If date input is wrong, error message for user saying "DoB input incorrectly, please use the format YYYY-MM-DD"

# If date input is too old, error message - "Please input a valid year"

# If date input is in future, error message - "You can't be below 0 years old!"