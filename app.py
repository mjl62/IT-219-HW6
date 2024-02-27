
"""
import sys
from typing import Callable, cast
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

def do_operation(op: str, x: Decimal, y: Decimal):
    if op == "add":
        return add(x, y)
    elif op == "subtract":
        return subtract(x, y)
    elif op == "multiply":
        return multiply(x, y)
    elif op == "divide":
        return divide(x, y)
    else:
        return "Not a valid operator"
        

def main():
    ''' Catch short input '''
    if len(sys.argv) < 4:
        print("Usage: python3 " + sys.argv[0] + " <value> <value> <operation>")
        exit(0)

    values = [ sys.argv[1], sys.argv[2] ]
    op = sys.argv[3]
    
    print(do_operation(op, Decimal(values[0]), Decimal(values[1])))
        

if __name__ == "__main__":
    main()
    """