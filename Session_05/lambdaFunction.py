'''
Lambda function= It is a small anonymous function that can take any number of arguments, but can only have one expression. It is also known as an inline function or a throw-away function.

syntax:
lambda arguments: expression

Eg: lambda x: x + 10
'''

def addTwoNumbers(x, y):
    return x + y

print(addTwoNumbers(5, 10))

# Using lambda function
add = lambda x, y: x + y
print(add(5, 10))

square = lambda x: x ** 2
print(square(5))

square = lambda x, y: x ** 2 + y
print(square(5, 10))

#Multiple variables in lambda function
multiply = lambda x, y, z : x * y * z
print(multiply(2, 3, 4))


#Lambda function within another function
def outerFunction(x):
    return lambda y: x + y

innerFunction = outerFunction(5)
print(innerFunction(10))