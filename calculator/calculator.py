''' Calculator, Calculation and Calculations classes '''

from decimal import Decimal
from typing import Callable, List
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    ''' Calculation object class '''
    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self) -> Decimal:
        ''' Return result of the calculation '''
        return self.operation(self.x, self.y)


class Calculator:
    '''
        Calculator
        Supports addition, subtraction, multiplication,
        and division.
        Uses Calculations for storing a history of operations
    '''
    @staticmethod
    def _perform_operation(
    x: Decimal,
    y: Decimal,
    operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        ''' Performs the operation given with x and y '''
        calculation = Calculation(x, y, operation)
        Calculations.store(calculation)
        return calculation.get_result()

    @staticmethod
    def add(x:Decimal, y:Decimal) -> Decimal:
        ''' Adds x and y and returns a decimal '''
        return Calculator._perform_operation(x, y, add)

    @staticmethod
    def subtract(x:Decimal, y:Decimal) -> Decimal:
        ''' Subtracts y from x and returns a decimal '''
        return Calculator._perform_operation(x, y, subtract)

    @staticmethod
    def multiply(x:Decimal, y:Decimal) -> Decimal:
        ''' Multiplies x by y and returns a decimal '''
        return Calculator._perform_operation(x, y, multiply)

    @staticmethod
    def divide(x:Decimal, y:Decimal) -> Decimal:
        ''' Divides x by y and returns a decimal '''
        return Calculator._perform_operation(x, y, divide)


class Calculations:
    ''' Stores calculations history '''

    history: List[Calculation] = []

    @classmethod
    def store(cls, calculation: Calculation):
        ''' Stores a calculation in the calculation history '''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        ''' Returns the current calculation history '''
        return cls.history

    @classmethod
    def get_latest(cls) -> Calculation:
        ''' Returns the latest calculation, or None otherwise '''
        if len(cls.history) == 0:
            return None
        return cls.history[-1]

    @classmethod
    def clear_history(cls) ->List[Calculation]:
        ''' Clears the calculation history '''
        cls.history.clear()
        return cls.history
