'''
    Operations
    Contains functions for mathematical operations
'''

def add(x, y):
    ''' Adds x and y and returns the result '''
    return x + y

def subtract(x, y):
    ''' Subtracts y from x and returns the result '''
    return x - y

def multiply(x, y):
    ''' Multiplies x by y and returns result '''
    return x * y

def divide(x, y):
    ''' Divides x by y and returns the result '''
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
