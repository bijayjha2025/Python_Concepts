'''
Statistics deals with collecting, analyzing, interpreting, presenting, and organizing data. It is a branch of mathematics that provides tools and techniques for understanding and making decisions based on data. Types: a. descriptive which involves summarizing and describing the main features of a dataset, and b. inferential which involves making predictions or inferences about a population based on a sample of data.
Descriptive statistics includes measures of central tendency (mean, median, mode) and measures of variability (range, variance, standard deviation). Inferential statistics includes hypothesis testing, confidence intervals, and regression analysis. Statistics is widely used in various fields such as business, economics, social sciences, healthcare, and many others to make informed decisions based on data analysis.
'''

#NumPy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. NumPy is widely used in scientific computing, data analysis, and machine learning due to its speed and ease of use. 

#NumPy provides a wide range of functionalities, including:
#1. Array creation and manipulation: NumPy allows us to create arrays of different shapes and sizes, and provides various functions to manipulate these arrays, such as reshaping, slicing, and indexing.
#2. Mathematical operations: NumPy provides a wide range of mathematical functions, including basic arithmetic operations, trigonometric functions, logarithmic functions, and more. These functions can be applied element-wise to arrays, making it easy to perform complex calculations on large datasets.
#3. Linear algebra: NumPy provides support for linear algebra operations, such as matrix multiplication, eigenvalue decomposition, and singular value decomposition. These operations are essential for many applications in machine learning and data analysis.

#To install NumPy, we can use the pip package manager by running the following command in the terminal:
#pip install numpy

import numpy as np
#Creating a NumPy array from a Python list
data = [1, 2, 3, 4, 5]
print("Type:", type(data))

print(data)

twoDList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
twoDArray = np.array(twoDList)

numpyArrayfromList = np.array(data)
print("Type:", type(numpyArrayfromList))
print("Array:", numpyArrayfromList)


#Creating float numpy array
floatArray = np.array([1.0, 2.0, 3.0])
print("Type:", type(floatArray))
print("Array:", floatArray)

#Creating boolean numpy array
boolArray = np.array([True, False, True])
print("Type:", type(boolArray))
print("Array:", boolArray)