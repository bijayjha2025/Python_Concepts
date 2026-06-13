# '''
# Modules in Python are files containing Python code that can be imported and used in other Python programs. They allow you to organize your code into reusable components, making it easier to manage and maintain. A module can contain functions, classes, variables, and runnable code. To use a module, you can import it using the import statement.

# In other words, modules allow us to use pre-written code in our programs, so we don't have to write everything from scratch.

# Types:
# i. Built-in Modules: These are modules that come with Python and are available for use without needing to install anything. Examples include math, random, datetime, sys, os etc.

# ii. User-defined Modules: These are modules that we create ourselves. We can write our own functions, classes, and variables in a Python file and then import that file as a module in another Python program.

# Note that we need to import a module before we can use its functions, classes, or variables. We can import a module using the import statement followed by the name of the module.
# '''

# # Example of using a built-in module (math)
# import math
# print(math.sqrt(16))  # sqrt gives the square root of a number
# print(math.pi)  # pi gives the value of π
# print(math.factorial(5))  # factorial gives the factorial of a number
# print(math.sin(math.pi/2))  # sin gives the sine of an angle (in radians)
# print(math.cos(0))  # cos gives the cosine of an angle (in radians)
# print(math.floor(3.7))  # floor gives the largest integer less than or equal to a number
# print(math.ceil(3.2))  # ceil gives the smallest integer greater than or equal to a number
# print(math.pow(2, 3))  # pow gives the value of a number raised to the power of another number


# #Another example of using a built-in module (random)
# import random
# print(random.randint(1, 10))  # randint gives a random integer between a specified range
# print(random.choice(['apple', 'banana', 'cherry']))  # choice gives a random element from a non-empty sequence
# print(random.shuffle([1, 2, 3, 4, 5]))  # shuffle randomly shuffles the elements of a list in place
# print(random.sample([1, 2, 3, 4, 5], 3))  # sample gives a random sample of specified size from a population
# print(random.random())  # random gives a random float number between 0.0 and 1.0
# print(random.uniform(1.0, 10.0))  # uniform gives a random float number between a specified range
# print(random.seed(42))  # seed initializes the random number generator with a specific seed value


# #Another example of using a built-in module (datetime)
# import datetime
# print(datetime.datetime.now())  # now gives the current date and time
# print(datetime.datetime(2022, 1, 1))  # datetime gives a specific date and time
# print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))  # strftime formats a datetime object into a string according to a specified format


# #Next built-in module is sys, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. It is always available.

# import sys
# print(sys.version)  # version gives the version of Python that is currently running
# print(sys.platform)  # platform gives the name of the platform on which Python is running
# print(sys.path)  # path gives a list of strings that specifies the search path for modules
# print(sys.exit())  # exit exits the Python interpreter


# #os module provides a way of using operating system dependent functionality. It allows us to interact with the underlying operating system in a portable way.

# import os
# print(os.name)  # name gives the name of the operating system dependent module imported


# #User-defined module example

# import myModule

# print(myModule.greet("Bijay"))
# print(myModule.add(5, 3))
# print(myModule.subtract(10, 4))
# print(myModule.multiply(6, 7))
# print(myModule.divide(15, 3))


#In Python, there are also external modules that are not included in the standard library but can be installed using package managers like pip. These modules provide additional functionality and can be used in your Python programs after installation. Examples of popular external modules include NumPy for numerical computing, Pandas for data manipulation, Matplotlib for data visualization, and Requests for making HTTP requests.

#In order to use an external module, we first need to install it using pip.

import pyjokes
print(pyjokes.get_joke()) #gets random joke from the pyjokes module


#Another example of using an external module (NumPy)
import numpy as np
print(np.array([1, 2, 3, 4, 5]))

#Another example of using an external module (Pandas)
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

