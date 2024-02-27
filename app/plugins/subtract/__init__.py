from app.command import Command
from typing import List
from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator
from multiprocessing import Queue

class SubtractCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        calculator = Calculator()
        # Convert args to decimal
        if (len(args) == 0):
           print(SubtractCommand.usage())
           return
        try:
            args = list(map(Decimal, args))
        except InvalidOperation:
            print(SubtractCommand.usage())
            return
        result = args.pop(0)
        for num in args:
            result = calculator.subtract(result, num)
        print(result)
        
        
    def menuText() -> str:
        return "Subtracts one or more numbers from the first number."
    
    def usage() -> str:
        return "Usage: subtract <decimal> <decimal>"
