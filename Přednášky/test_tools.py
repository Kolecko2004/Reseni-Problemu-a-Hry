from tools import sum_digits
from testing import assert_equal


def test_empty_string():
    observed = sum_digits("")
    expected = 0
    return assert_equal(observed, expected)


def tes_chars():
    observed = sum_digits("abc")
    expected = 0
    return assert_equal(observed, expected)


test_empty_string()
tes_chars()
