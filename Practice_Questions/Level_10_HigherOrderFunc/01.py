'''
Difference between map, filter, and reduce functions

map() => changes each item, does not remove anything
marks = [50, 60, 70, 80, 90]
scaledMarks = list(map(lambda x: x * 2, marks))


filter() => removes items based on a condition, keeps only what we want
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, numbers))

reduce() => reduces the list to a single value, combines all items into one; It is available in Python's functools module.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
'''

'''
# Explain the difference between higher order function, closure and decorator

a. Higher Order Function: It is a function that either accepts another function as an argument or return another function.

b. Closure: A closure is a function that remembers the variables from its outer function even after the outer function has finished executing. It allows the inner function to access the variables of the outer function.

c. Decorator: A decorator is a special type of higher-order function that takes a function as an argument and returns a new function that enhances or modifies the behavior of the original function. Decorators are often used to add functionality to existing functions without modifying their code.
Decorators are built using closures and higher-order functions. They allow you to wrap a function with additional functionality, such as logging, authentication, or timing, without changing the original function's code.


'''