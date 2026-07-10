'''
PIP = PIP stands for Preferred Installer Program. It is a package management system used to install and manage software packages written in Python. PIP allows users to easily download and install libraries and dependencies from the Python Package Index (PyPI) or other repositories.

Syntax: pip install package_name
Example: pip install pyjokes
To check, use: pip --version

'''

#Numpy is a popular Python library used for numerical computing and data manipulation. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. Numpy is widely used in scientific computing, data analysis, and machine learning applications.

from gettext import install

import numpy as np
import pip
import requests
print(np.version.version)

list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1) #Converting list to numpy array
print(array1)
print(len(array1))
print(type(array1))

nparray1 = np.array([[1, 2, 3], [4, 5, 6]]) #Creating a 2D numpy array
print(nparray1)


#Next panda

import pandas as pd
print(pd.__version__)


#To uninstall packages, we can use: pip uninstall package_name

#to see the installed packages, we can use: pip list

#to see information about a packagae, we can use: pip show package_name

#pip freeze is used to generate a list of installed packages and their versions in the current Python environment. It is commonly used to create a requirements file that can be shared with others or used to recreate the same environment on a different machine.

#Reading from URL: 
# We can use the requests library to read data from a URL. The requests library is a popular Python library for making HTTP requests and handling responses. It provides a simple and convenient way to send GET, POST, PUT, DELETE, and other types of HTTP requests to web servers and APIs as:
import requests
url = 'https://jsonplaceholder.typicode.com/todos/1'

# get the response from the URL
response = requests.get(url)
print(response.status_code) #Printing the status code of the response
print(response.json()) #Printing the JSON response from the URL
print(type(response.json())) #Printing the type of the JSON response


# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text
print(text[:500])

