''' Test functions for Calculation object '''

from calculator.calculator import Calculation
from calculator.operations import add, subtract

def test_calculation():
    '''
        Tests Calculation functionality, uses two different operations to ensure it
        is working for multiple cases.
    '''
    calc_add = Calculation(126, 24, add)
    calc_subtract = Calculation(125, 25, subtract)
    assert calc_add.get_result() == 150 and calc_subtract.get_result() == 100
