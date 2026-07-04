'''
Higher Order Functions:
In Python, functions are first-class citizens, meaning we can perform following operations on them:
A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable

Higher-order functions are functions that operate on other functions, either by taking them as arguments or by returning them. It simply means that a higher-order function can accept a function as an argument, return a function, or both. This allows for more abstract and flexible programming patterns.

'''

# Example of a function as a parameter
def sumNumbers(nums):
    return sum(nums)

def higherOrderFunction(f, lst):
    summation = f(lst)
    return summation
result = higherOrderFunction(sumNumbers, [1, 2, 3, 4, 5])
print(result)

# In this example, we have defined a function sumNumbers that takes a list of numbers and returns their sum. Then, we have defined a higher-order function higherOrderFunction that takes a function f and a list lst as parameters. Inside the higherOrderFunction, we call the function f with the list lst and return the result. Finally, we call higherOrderFunction with sumNumbers and a list of numbers, and print the result.


# Function as a return value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return abs(x)

def higherOrderFunc(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    else:
        return None
    

result = higherOrderFunc('square')
print(result(5))

result1 = higherOrderFunc('cube')
print(result1(3))

result2 = higherOrderFunc('absolute')
print(result2(-10))


#In this example, we have defined three functions: square, cube, and absolute. Then, we have defined a higher-order function higherOrderFunc that takes a string type as a parameter. Inside the higherOrderFunc, we check the value of type and return the corresponding function. Finally, we call higherOrderFunc with different types and print the results of calling the returned functions with specific arguments.
