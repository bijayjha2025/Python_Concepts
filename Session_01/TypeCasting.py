
#By default, Python take input as string, which can cause issues when we want to perform mathematical operations on the input. To avoid this, we can use type casting to convert the input from string to the desired data type (like int or float). So, Typecasting or type conversion can be defined as the process of converting a value from one data type to another. In Python, we can perform typecasting using built-in functions like int(), float(), str(), etc.

'''
There are two types of typecasting in Python:
1. Implicit Typecasting: This is when Python automatically converts one data type to another without the programmer's intervention. For example, when we add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
2. Explicit Typecasting: This is when the programmer manually converts one data type to another using built-in functions. For example, if we want to convert a string to an integer, we can use the int() function to explicitly cast the string to an integer.
'''


x = input("Enter a number: ")
print("You entered:", x)
y = input("Enter another number: ")
print("You entered:", y)
print(type(x), type(y))
print("the sum of x and y is:", x + y)

print(int(x)+ int(y))
print(type(int(x)), type(int(y)))

print(float(x) + float(y))
print(type(float(x)), type(float(y)))

print(bool(x), bool(y))
print(type(bool(x)), type(bool(y)))


print(bool())
print(bool(0))

print(bool(1))
print(bool(-1))
print(bool("Okay"))

'''
#In Python, the following values are considered False in a boolean context:
#1. None
#2. False
#3. Zero of any numeric type (0, 0.0, 0j)
#4. Empty sequences and collections (e.g., '', [], (), {})

Any other value is considered True in a boolean context. This includes non-empty strings, non-zero numbers, and non-empty collections.
'''

#Implicit Typecasting

a = 5
b = 3.14

print(a + b)
print(type(a + b))


c = 10
d = 2 + 3j

print(c + d)
print(type(c + d))


e = 7
f = "Hello"

#But printing (e+f) in the case will raise a TypeError because we cannot add an integer and a string together without explicit typecasting.

h = 10
i = "20"
print(h + int(i))
print(str(h) + i)
print(type(int(i)), type(str(h)))

