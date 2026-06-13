#This is my module file, which I want to use in another Python program.

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
    
