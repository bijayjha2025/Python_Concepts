'''
Packing and Unpacking in Python
It is a technique that allows you to assign multiple values to a single variable or unpack values from a collection into separate variables. It is commonly used with tuples, lists, and dictionaries. It is achieved using * for tuples and lists, and ** for dictionaries.
'''

def sumOfFiveNumbers(a, b, c, d, e):
    return a + b + c + d + e

listNew = [1, 2, 3, 4, 5]

#Unpacking the list into individual variables
print(sumOfFiveNumbers(*listNew))


#We can also use unpacking with in built range function
numbers = range(1, 6)
print(list(numbers))

arguments = [8,9]
numbers = range(*arguments)
print(numbers)


#A list and tuple can be unpacked as:
countries = ['Nepal', 'India', 'China', 'Bhutan', 'Bangladesh']
nep, ind, *others = countries
print(nep)
print(nep, ind, others)

numbersNew = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbersNew
print(one, middle, last)


#Unpacking a dictionary can be done as follows:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
name, age, city = person.values()
print(name, age, city)