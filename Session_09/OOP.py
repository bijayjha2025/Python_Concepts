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


#Object methods: Object methods are functions that are defined inside a class and can be called on an object of that class. They can access and modify the attributes of the object.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        
        
e = Employee("Kale", "Manager", 50000)
print(e.displayInfo())


#Object default methods: Object default methods are special methods that are automatically called by Python when certain operations are performed on an object. These methods have double underscores before and after their names, and they allow us to customize the behavior of our objects.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book2)


#Method to modify class default methods: We can also modify the default methods of a class to customize the behavior of our objects. For example, we can modify the __str__() method to return a different string representation of our object.

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"{self.title} directed by {self.director} ({self.year})"
    
    def __repr__(self):
        return f"Movie({self.title}, {self.director}, {self.year})"
    
movie1 = Movie("Inception", "Christopher Nolan", 2010)
print(movie1)
movie2 = Movie("The Dark Knight", "Christopher Nolan", 2008)
print(movie2)