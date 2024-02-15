'''
    Test for Calculator functoinality
'''

from calculator.calculator import Calculator, Calculations

calculator = Calculator()

def test_add():
    ''' Test calculator addition '''
    assert calculator.add(1,3) == 4

def test_subtract():
    ''' Test calculator subtraction '''
    assert calculator.subtract(6, 3) == 3

def test_multiply():
    ''' Test calculator multiplication '''
    assert calculator.multiply(5, 3) == 15

def test_divide():
    ''' Test calculator division '''
    assert calculator.divide(10, 2) == 5

def test_calculation_store():
    ''' Test that information from the calculations are stored properly '''
    calculator.add(2,5)
    calculation = Calculations.get_history()[-1]
    assert calculation.x == 2 and calculation.y == 5 and calculation.get_result() == 7

def test_history():
    '''
        Tests history by checking that addition and
        multiplication Calculations worked by checking their functions 
    '''
    history = Calculations.get_history()
    assert history[0].get_result() == 4 and history[2].get_result() == 15

def test_clear_history():
    ''' Tests the function that clears the history '''
    assert len(Calculations.clear_history()) == 0

def test_get_latest():
    ''' Tests getting the latest Calculation from history '''
    calculator.add(2,5)
    assert Calculations.get_latest()

def test_get_latest_fail():
    ''' Tests getting the latest Calculation from history '''
    Calculations.clear_history()
    assert Calculations.get_latest() is None
