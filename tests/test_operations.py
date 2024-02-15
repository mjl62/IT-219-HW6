''' 
    Tests for operations 
'''

import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    ''' Test if the addition function works '''
    assert add(5, 3) == 8

def test_subtract():
    ''' Test if the subtraction function works '''
    assert subtract(5, 3) == 2

def test_multiply():
    ''' Test if the multiplication function works '''
    assert multiply(5, 3) == 15

def test_divide():
    ''' Test if the division function works '''
    assert divide(15, 3) == 5

def test_divide_by_zero():
    ''' Test if division function raises error on 0 in denominator '''
    with pytest.raises(ValueError):
        divide(5, 0)
