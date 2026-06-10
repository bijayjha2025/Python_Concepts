
'''
Indentation => Indentation means the spaces at the beginning of a code line. Unlike other languages which uses this to improve readability, in Python it is a syntax requirement. It is used to define the scope of loops, functions, and other code blocks. Consistent indentation is crucial in Python, as it determines how the code is grouped together. If the indentation is not consistent, it will lead to an Indentation error.
'''
a = 5
b = 5
if a == b:
    print("a and b are equal.")


'''
Comments => Comments are used to explain the code and make it more readable. In Python, comments are created using the hash symbol (#). Anything following the # on the same line is considered a comment and is ignored by the Python interpreter. Comments can be used to describe what a particular block of code does, to provide context for future reference, or to temporarily disable code during debugging.
'''

print("Hello") #This is a comment and it will not affect the execution of the code. It will not be printed and is only for the programmer's reference.


'''
Docstrings => Docstrings are a special type of comment used to document functions, classes, and modules in Python. They are enclosed in triple quotes (""" """) and can span multiple lines. Docstrings provide a convenient way to associate documentation with code elements, making it easier for developers to understand the purpose and usage of functions, classes, and modules.

'''

# Example of a function with a docstring
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# To access the docstring of a function, we can use the __doc__ attribute:
print(add.__doc__)


'''
PEP 8 => PEP 8 is the style guide for Python code. It provides guidelines and best practices on how to write Python code in a way that is readable and consistent. Following PEP 8 helps improve the readability of code and makes it easier for developers to collaborate on projects. Some of the key guidelines in PEP 8 include:
- Use 4 spaces per indentation level
- Use blank lines to separate functions and classes
- Use descriptive variable names
- Use spaces around operators and after commas
'''

