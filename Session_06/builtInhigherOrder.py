'''
Built-in higher order functions:
a. map() function: The map() function applies a given function to all items in an iterable (like a list) and returns a new iterable with the results. It takes two arguments: the function to apply and the iterable to process.
b. filter() function: The filter() function filters elements from an iterable based on a given condition (a function that returns True or False). It returns a new iterable containing only the elements that satisfy the condition.
c. reduce() function: The reduce() function, which is part of the functools module, applies a binary function cumulatively to the items of an iterable, reducing the iterable to a single value. It takes two arguments: the function to apply and the iterable to process.
'''

#map() function example

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
squaredNumbers = list(map(square, numbers))
print(squaredNumbers)

#Another example
strings = ['apple', 'banana', 'cherry']
def upper(string):
    return string.upper()

upperStrings = list(map(upper, strings))
print(upperStrings)

#Another example
names = ["Haha", "Hehe", "Hihi"]
def greet(name):
    return f"Hello, {name}!"
greetings = list(map(greet, names))
print(greetings)

#Let's apply it with lambda function
names = ["Haha", "Hehe", "Hihi"]
greetings = list(map(lambda name: name.lower(), names))
print(greetings)