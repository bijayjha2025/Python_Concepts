'''
Object-Oriented Programming (OOP) in Python: Python allow us to create classes and objects, which are the building blocks of OOP. A class is a blueprint for creating objects, and an object is an instance of a class. OOP allows us to model real-world entities and their behaviors in our programs.

syntax to create class:
class ClassName:
    #class attributes and methods

'''
# class Person:
#     pass
# print(Person)


#creating an object of the class Person, we should call the class as a function, which will return an object of the class.

# person1 = Person()
# print(person1)


#Class constructor: A class constructor is a special method that is automatically called when an object of the class is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John Cena", 52)
print(person1.name)
print(person1.age)


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

student1 = Student("Karl Max", 20, "S12345")
print(student1.name)
print(student1.age)
print(student1.student_id)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
print(car1.make)
print(car1.model)
print(car1.year)