#Reduce function: It is used to apply a function cumulatively to the items of an iterable, reducing the iterable to a single value. The reduce() function is part of the functools module and takes two arguments: a function and an iterable. It applies the function to the first two items of the iterable, then applies it to the result and the next item, and so on, until all items have been processed.

#Example
from functools import reduce #reduce is not a built-in function, it is part of the functools module, it must be imported before using it

numbers = [1, 2, 3, 4, 5]
def addTwoNumbers(x, y):
    return x + y

total = reduce(addTwoNumbers, numbers)
print(total)

#Another example using lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(lambda x, y: x + y, numbers)
print(total)

#To find the product of all numbers in a list
numbers = [1, 2, 3, 4, 5]
def multiplyTwoNumbers(x, y):
    return x * y

product = reduce(multiplyTwoNumbers, numbers)
print(product)


#find the maximum number in a list
numbers = [1, 2, 3, 4, 5]
def findMax(x, y):
    if x > y:
        return x
    return y

maxNumber = reduce(findMax, numbers)
print(maxNumber)

#find the minimum number in a list
numbers = [1.5, 3.7, 2.1, 4.8, 0.9]
def findMin(x, y):
    if x < y:
        return x
    return y

minNumber = reduce(findMin, numbers)
print(minNumber)