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


#Packing lists
def sumAll(*args):
    s = 0
    for i in args:
        s += i

    return s

print(sumAll(1, 2, 3, 4, 5))
print(sumAll(10, 20, 30))


#Packing dictionaries
def packingPersonalInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    return kwargs

print(packingPersonalInfo(name='John', age=30, city='New York'))


#Spreading in Python: It is a technique that allows you to expand the elements of an iterable (like a list or tuple) into individual elements. It is achieved using * for tuples and lists, and ** for dictionaries.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(list3)

countries1 = {'Nepal': 'Kathmandu', 'India': 'New Delhi'}
countries2 = {'China': 'Beijing', 'Bhutan': 'Thimphu'}
countries3 = {**countries1, **countries2}
print(countries3)


#Enumerate in Python: It is a built-in function that adds a counter to an iterable and returns it as an enumerate object. It is commonly used in loops to get both the index and the value of each item in the iterable.

for index, item in enumerate(['apple', 'banana', 'cherry']):
    print(index, item)


countries = ['Nepal', 'India', 'China', 'Bhutan', 'Bangladesh']
for index, country in enumerate(countries):
    print(f"{index}: {country}")


#Zip in Python: It is a built-in function that takes two or more iterables and returns an iterator that aggregates elements from each iterable. It is commonly used to combine multiple lists or tuples into a single iterable.
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'red']
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")


#Another example of using zip function
names = ['Karl', 'Einstein', 'Newton']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


#Practice Question: names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

namesCountry = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordicCountries, es, ru = namesCountry[:5], namesCountry[5], namesCountry[6]
print(nordicCountries, es, ru)