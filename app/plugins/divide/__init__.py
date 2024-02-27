from app.command import Command
from typing import List
from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator
from multiprocessing import Queue

class DivideCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        calculator = Calculator()
        # Convert args to decimal
        if (len(args) == 0):
           print(DivideCommand.usage())
           return
        try:
            args = list(map(Decimal, args))
        except InvalidOperation:
            print(DivideCommand.usage())
            return
        result = args.pop(0)
        for num in args:
            result = calculator.divide(result, num)
        print(result)
        
    def menuText() -> str:
        return "Divides two or more numbers."
    
    def usage() -> str:
        return "Usage: divide <decimal> <decimal>"
