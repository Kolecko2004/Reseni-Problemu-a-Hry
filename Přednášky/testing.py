from tools import sum_digits
import sys

def assert_equal(observed, expected):
    observed = sum_digits("")
    expected = 0
    if observed == expected:
        print("Everything is OK :)")
        return True
    else:
        print("Test failed :(")
        print(f'Expected: {expected} but function gave me: {observed}')
        return False
    #print(sum_digits("ofudasph213oh4oih52h34b5k2"))

def run_tests():
    frame = sys._getframe(1)
    for symbol, value in fra,e.f_globals.items():
        if symbol.startswith("test_"):
            test_func = value
            result.append(test_func())
        print("========= Test Results")
        print(f'{len(results)}test ran')