'''
Data Types in Python
Data types simply means what type of data a variable can hold. In Python, there are several built-in data types such as:
1. Numeric Types: int, float, complex
2. Sequence Types: list, tuple, range
3. Text Type: str
4. Mapping Type: dict
5. Set Types: set, frozenset
6. Boolean Type: bool
7. Binary Types: bytes, bytearray, memoryview
8. None Type: NoneType

Each data type has its own characteristics and is used for different purposes in programming. For example, integers (int) are used for whole numbers, floats are used for decimal numbers, strings (str) are used for text, lists are used for ordered collections of items, dictionaries (dict) are used for key-value pairs, and so on. Understanding data types is crucial for writing efficient and effective code in Python.
'''

#type() function => It is a built-in function in Python that is used to determine the type of a variable or value. It returns the data type of the object passed as an argument.

#1. Numeric Types
#Integer (int) => It is a whole number without a decimal point. It can be positive, negative, or zero. For example:
a, b , c = 10, -5, 0
print(a)
print(type(a), type(b), type(c))

#Float (float) => It is a number that has a decimal point. It can also be in exponential form. For example:
x, y = 3.14, -0.001
print(x)
print(type(x), type(y))


#Complex (complex) => It is a number that has a real part and an imaginary part. The imaginary part is denoted by 'j' in Python. For example:
z = 2 + 3j
print(z)
print(type(z))

#2. Text Type
#String (str) => It is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). For example:
s1 = 'Hello'
s2 = "World"
s3 = '''This is a multi-line string.'''
print(s1)
print(type(s1), type(s2), type(s3))

c4 = 'v' #In above example, we have assigned a single character 'v' to the variable c4. In Python, there is no separate data type for single characters; they are treated as strings of length 1. Therefore, the type of c4 will be <class 'str'>.
print(c4)
print(type(c4))


#3. Boolean Type
#Boolean (bool) => It is a data type that can only have two values: True or False. It is often used in conditional statements and logical operations. For example:

isValid = True
isEmpty = False
print(isValid)
print(isEmpty)
print(type(isValid), type(isEmpty))


#4. None Type
#NoneType (None) => It is a special data type that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or to signify the end of a function. For example:

result = None
print(result)
print(type(result))

'''
Mutable vs Immutable Data Types
In Python, data types can be classified as mutable or immutable based on whether their values can be changed after they are created.
1. Mutable Data Types: These are data types that can be modified after they are created. Examples include lists, dictionaries, sets. For instance, we can change the elements of a list or add new key-value pairs to a dictionary.
2. Immutable Data Types: These are data types that cannot be modified after they are created. Examples include integers, floats, strings, tuples. For instance, once we create a string, we cannot change its characters; instead, we would need to create a new string if we want to modify it.
'''

#Sequence Types
#List (list) => It is an ordered collection of items that can be of different data types. Lists are mutable, which means we can change their contents after they are created. For example:
list1 = [1, 2, 3, "Hello", True]
print(list1)
print(type(list1))

#Tuple (tuple) => It is an ordered collection of items that can be of different data types. Tuples are immutable, which means we cannot change their contents after they are created. For example:
tuple1 = (1, 2, 3, "Hello", True)
print(tuple1)
print(type(tuple1))

#Range (range) => It is a sequence of numbers that is commonly used for looping a specific number of times in for loops. The range function generates a sequence of numbers based on the specified start, stop, and step values. For example:
range1 = range(5) # Generates numbers from 0 to 4
print(range1)
print(type(range1))

#Mapping Type
#Dictionary (dict) => It is an unordered collection of key-value pairs. Dictionaries are mutable, which means we can change their contents after they are created. For example:
dict1 = {"name": "Alice", "age": 30, "isStudent": True}
print(dict1)
print(type(dict1))

#Set Types
#Set (set) => It is an unordered collection of unique items. Sets are mutable, which means we can change their contents after they are created. For example:
set1 = {1, 2, 3, "Hello", True}
print(set1)
print(type(set1))

#Frozenset (frozenset) => It is an unordered collection of unique items that is immutable, which means we cannot change its contents after it is created. For example:
frozenset1 = frozenset([1, 2, 3, "Hello", True])
print(frozenset1)
print(type(frozenset1))

#Binary Types
#Bytes (bytes) => It is an immutable sequence of bytes, which is used to represent binary data. For example:
bytes1 = b"Hello"
print(bytes1)
print(type(bytes1))

#Bytearray (bytearray) => It is a mutable sequence of bytes, which is used to represent binary data. For example:
bytearray1 = bytearray(b"Hello")
print(bytearray1)
print(type(bytearray1))

'''
Ordered vs Unordered Data Types
In Python, data types can also be classified as ordered or unordered based on whether the elements in the data type have a specific order or not.
1. Ordered Data Types: These are data types where the elements have a specific order, and we can access them using their index. Examples include lists, tuples, and strings. For instance, in a list, the first element is at index 0, the second element is at index 1, and so on.
2. Unordered Data Types: These are data types where the elements do not have a specific order, and we cannot access them using their index. Examples include sets and dictionaries. For instance, in a set, the elements are not stored in any particular order, and we cannot access them using an index. In a dictionary, the key-value pairs are also not stored in any particular order, and we access the values using their corresponding keys rather than an index.

'''

'''
Python is a dynamically typed language, meaning that we do not need to declare the data type of a variable when we create it. A same variable can hold different types of data at different times during execution.
'''