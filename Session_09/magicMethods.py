'''
Magic Methods in Python: It is a special type of method that starts and ends with double underscores (__). These methods are also known as dunder methods (double underscore methods). They allow us to define the behavior of our objects for built-in operations, such as addition, subtraction, string representation, and more. By implementing magic methods in our classes, we can customize how our objects behave in different contexts.
'''
# Example 1: using __init__ and __str__ magic methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
    

person1 = Person("Neil", 30)
print(person1)


# Example 2: using __add__ magic method to add two objects of a class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)


# Example 3: using __len__ magic method to get the length of an object
class customList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    

my_list = customList([1, 2, 3, 4, 5])
print(len(my_list))

#These are just a few examples of magic methods in Python. There are many more magic methods available that allow us to customize the behavior of our objects for various operations. Some other commonly used magic methods include __sub__, __mul__, __truediv__, __eq__, __lt__, __gt__, and many more. By implementing these magic methods in our classes, we can create more intuitive and user-friendly objects that behave like built-in types in Python.