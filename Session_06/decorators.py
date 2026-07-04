'''
Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. They are often used for logging, access control, memoization, and more.
A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function. Decorators are often used to wrap functions in order to extend their behavior without modifying their code.
'''

def greeting():  #This is a normal function
    return "Welcome to Python Decorators!"

def upperCaseDecorator(func):
    def wrapper():
        func = greeting()  # Call the original function
        return func.upper()  # Modify the result to uppercase
    return wrapper  # Return the wrapper function

message = upperCaseDecorator(greeting)  # Apply the decorator to the greeting function
print(message())  # Call the decorated function and print the result 


# Another example of a decorator that takes arguments, we will use higher order function

def upperCaseDecorator(function):
    def wrapper():
        func = function()
        makeUpperCase = func.upper()
        return makeUpperCase
    
    return wrapper

@upperCaseDecorator
def greeting():
    return "Welcome to Python Decorators!"