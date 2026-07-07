
# 1. Syntax Error: This occurs when the code is not written in correct syntax. For example, missing a colon at the end of a for loop or if statement.

Example of Syntax Error:
for i in range(5)
    print(i)


# 2. Name Error: This occurs when a variable or function name is not defined or is misspelled.
#Example of Name Error:
print(dontKnowVariable)


# 3. Index Error: This occurs when trying to access an index that is out of range for a list or string.
#Example of Index Error:
myList = [1, 2, 3]
print(myList[5])  # Trying to access index 5 which does not exist


# 4. Module Not Found Error: This occurs when trying to import a module that does not exist or is not installed.
#Example of Module Not Found Error:
import nonExistentModule  # Trying to import a module that does not exist

# 5. Attribute Error: This occurs when trying to access an attribute or method that does not exist for a particular object.
# Example of Attribute Error:
import math
print(math.PI)

# 6. Key Error: This occurs when trying to access a key that does not exist in a dictionary.
# Example of Key Error:
dictionary = {'name': 'John', 'age': 30}
print(dictionary['gender'])  # Trying to access a key that does not exist

# 7. Type Error: This occurs when an operation or function is applied to an object of an inappropriate type.
# Example of Type Error:
print("Hello, World!" + 5)  # Trying to concatenate a string and an integer


# 8. Import Error: This occurs when there is an error in importing a module or package.
# Example of Import Error:
from math import power
print(power(2, 3))


# 9. Value Error: This occurs when a function receives an argument of the correct type but an inappropriate value.
# Example of Value Error:
int("Hello")  # Trying to convert a string that cannot be converted to an integer

# 10. ZeroDivisionError: This occurs when trying to divide a number by zero.
# Example of ZeroDivisionError:
print(10 / 0)  # Trying to divide by zero