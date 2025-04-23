# test_your_module.py
import pytest
from try_actions import sum
from try_actions import mul
from try_actions import sub

def test_sum():
    assert sum(3, 5) == 8

def test_sum():
    assert sum("hello", "world") == "helloworld"

def test_sum():
    assert sum([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_mul():
    assert mul(3, 5) == 15

def test_mul():
    assert mul("hello", 3) == "hellohellohello"

def test_mul():
    assert mul([1, 2], 3) == [1, 2, 1, 2, 1, 2]

def test_sub():
    assert sub(10, 5) == 5

def test_sub():
    assert sub(1, 2) == -1

def test_sub():     
    assert sub([1, 2], [3, 1]) == [-2, 1]
