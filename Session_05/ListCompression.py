'''
List compression = It is a compact way to create a list in python. It is a one liner code that can be used to create a new list from an existing list or any other iterable object. It is also known as list comprehension.

syntax:
[expression for i in iterable if condition]

'''
# Ways of changing strings to lists

#First way
string = "Hello, World!"
lst = list(string)
print(lst)

#Second way using list comprehension
lst1 = [i for i in string]
print(lst1)

#Another example of list comprehension
numbers = [i for i in range(11)]
print(numbers)

#It is also possible to do mathematical operations in list comprehension.

numbers2 = [i**2 for i in range(11)]
print(numbers2)

#It is also possible to make list of tuples
numbers3 = [(i, i**2) for i in range(11)]
print(numbers3)


#List comprehension can be combined with if expression
evenNumbers = [i for i in range(11) if i % 2 == 0]
print(evenNumbers)

oddNumbers = [i for i in range(21) if i %2 != 0]
print(oddNumbers)


# Let's filter out positive numbers from a list using list comprehension
numbersList = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
positiveNumbers = [num for num in numbersList if num > 0]
print(positiveNumbers)

#Flattening 2d array using list comprehension
list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenedList = [num for sublist in list2d for num in sublist]
print(flattenedList)