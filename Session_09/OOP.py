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


# Inheritance: Inheritance is a mechanism in OOP that allows us to create a new class based on an existing class. The new class inherits the attributes and methods of the existing class, and we can also add new attributes and methods to the new class.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog") #super() function is used to call the constructor of the parent class (Animal) and initialize the name and species attributes. The breed attribute is specific to the Dog class, so we initialize it separately.
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"
    
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Tabby")
#In the above example, we have defined a parent class Animal with a constructor that initializes the name and species attributes. We have also defined a method make_sound() that is meant to be overridden by the child classes.
print(dog1.make_sound())
print(cat1.make_sound())


#Overriding parent class methods: In the above example, we have overridden the make_sound() method in the Dog and Cat classes to provide their own implementation of the method. When we call the make_sound() method on a Dog object, it returns "Woof!", and when we call it on a Cat object, it returns "Meow!".


class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Bird")
        self.color = color

    def make_sound(self):
        return "Chirp!"
    
bird1 = Bird("Tweety", "Yellow")
print(bird1.make_sound())
# Here we have defined a new class Bird that inherits from the Animal class. We have overridden the make_sound() method to return "Chirp!" when called on a Bird object.


#Polymorphism: Polymorphism is a concept in OOP that allows us to use a single interface to represent different types of objects. In Python, we can achieve polymorphism by defining methods with the same name in different classes.

class Brands:
    def showBrand(self):
        return "This is a brand."
    
class Nike(Brands):
    def showBrand(self):
        return "This is Nike brand."
    

class Adidas(Brands):
    def showBrand(self):
        return "This is Adidas brand."
    

shoe = Brands()
nike_shoe = Nike()
print(shoe.showBrand())
print(nike_shoe.showBrand())

#In this example, we have defined a parent class Brands with a method showBrand(). We have also defined two child classes Nike and Adidas that inherit from the Brands class and override the showBrand() method to provide their own implementation. When we call the showBrand() method on a Brands object, it returns "This is a brand.", and when we call it on a Nike object, it returns "This is Nike brand.".



# Abstraction: Abstraction is a concept in OOP that allows us to hide the implementation details of an object and expose only the essential features. In Python, we can achieve abstraction by defining abstract classes and methods.

from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def deviceInfo(self):
        pass

class Laptop(Device):
    def deviceInfo(self):
        return "This is a laptop."
    

class Smartphone(Device):
    def deviceInfo(self):
        return "This is a smartphone."
    

laptop = Laptop()
smartphone = Smartphone()
print(laptop.deviceInfo())
print(smartphone.deviceInfo())

#In this example, we have defined an abstract class Device with an abstract method deviceInfo(). We have also defined two concrete classes Laptop and Smartphone that inherit from the Device class and provide their own implementation of the deviceInfo() method. When we call the deviceInfo() method on a Laptop object, it returns "This is a laptop.", and when we call it on a Smartphone object, it returns "This is a smartphone.".

# Encapsulation: Encapsulation is a concept in OOP that allows us to restrict access to the internal state of an object and protect it from unauthorized access or modification. In Python, we can achieve encapsulation by using private attributes and methods.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
    

customer_account = BankAccount("123456789", 1000)
customer_account.deposit(500)
customer_account.withdraw(200)
print(customer_account.get_balance())


#super(): The super() function is used to call the constructor of the parent class and initialize the attributes of the child class. It allows us to reuse the code in the parent class and avoid duplication.


