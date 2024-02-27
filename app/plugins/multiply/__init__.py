from app.command import Command
from typing import List
from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator
from multiprocessing import Queue

class MultiplyCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        calculator = Calculator()
        # Convert args to decimal
        if (len(args) == 0):
           print(MultiplyCommand.usage())
           return
        try:
            args = list(map(Decimal, args))
        except InvalidOperation:
            print(MultiplyCommand.usage())
            return
        result = args.pop(0)
        for num in args:
            result = calculator.multiply(result, num)
        print(result)
        
    def menuText() -> str:
        return "Multiplies two or more numbers."
    
    def usage() -> str:
        return "Usage: multiply <decimal> <decimal>"
