# test_your_module.py
import pytest
from try_actions import sum

def test_sum_adds_numbers():
    assert sum(3, 5) == 8

def test_sum_adds_strings():
    assert sum("hello", "world") == "helloworld"

def test_sum_adds_lists():
    assert sum([1, 2], [3, 4]) == [1, 2, 3, 4]
