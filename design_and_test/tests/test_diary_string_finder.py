
import pytest
from lib.diary_string_finder import *

def test_no_input_returns_error():
    with pytest.raises(Exception) as err:
        diary_string_finder([], "")
    err_mess = str(err.value)
    assert err_mess == "Both inputs missing"

def test_no_list_input_returns_error():
    with pytest.raises(Exception) as err:
        diary_string_finder([], "qwertyuiop")
    err_mess = str(err.value)
    assert err_mess == "List input missing"

def test_no_string_input_returns_error():
    with pytest.raises(Exception) as err:
        diary_string_finder(["as", "df", "ghj", "kl"], "")
    err_mess = str(err.value)
    assert err_mess == "String input missing"

def test_both_inputs_present_no_keyword_included():
    assert diary_string_finder(["qwerity", "zxcv", "loikmniju"], "#TODO") == "#TODO not found in notes"

def test_both_inputs_present_keyword_included():
    assert diary_string_finder(["qwerty", "fr#TODOcd", "loikmnju"], "#TODO") == "fr#TODOcd"