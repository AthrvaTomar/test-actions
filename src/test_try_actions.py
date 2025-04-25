# test_your_module.py
import pytest
from try_actions import sum
from try_actions import mul
from try_actions import sub

def test_sum():
    assert sum(3, 5) == 8
    assert sum(4,3) ==7
    assert sum(110,10) == 120

def test_mul():
    assert mul(3, 5) == 35
    assert mul(9,11) == 99
    
def test_sub():
    assert sub(10, 5) == 5
    assert sub(10,20) == -10
