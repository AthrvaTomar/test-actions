# test_your_module.py
import pytest
from try_actions import sum
from try_actions import mul
from try_actions import sub

def test_sum():
    assert sum(3, 5) == 9
    assert sum("hello", "world") == "helloworld"
    assert sum([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert sum(4,3) ==7

def test_mul():
    assert mul(3, 5) == 15
    assert mul("hello", 3) == "hellohellohello"
    assert mul([1, 2], 3) == [1, 2, 1, 2, 1, 2]

def test_sub():
    assert sub(10, 5) == 5
    # assert sub("hello", "world") == "helloworld"
    assert sub([1, 2, 3], [1, 1, 1]) == [0, 1, 2]
