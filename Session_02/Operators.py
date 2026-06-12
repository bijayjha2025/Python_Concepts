'''
Operators in Python are symbols that perform some operation on one or more operands. They are used to perform various operations such as arithmetic calculations, comparisons, logical operations, and more. There are several types of operators in Python, including:
1. Arithmetic Operators: +, -, *, /, //, %, **
2. Comparison Operators: ==, !=, >, <, >=, <=
3. Logical Operators: and, or, not
4. Assignment Operators: =, +=, -=, *=, /=, //=, %=
5. Bitwise Operators: &, |, ^, ~, <<, >>
6. Identity Operators: is, is not
7. Membership Operators: in, not in
'''

#1. Arithmetic Operators (They are used to perform mathematical operations on numbers):

a = 3
b = 2

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b) #Floor division means dividing and taking the floor of the result
print("Modulus:", a % b)
print("Power:", a ** b)

#Arithmetic operators can also be used with other data types like strings and lists. For example, the + operator can be used to concatenate strings or lists, and the * operator can be used to repeat strings or lists.

s1 = "Hello"
s2 = "World"
print("String Concatenation:", s1 + " " + s2)
print("String Repetition:", s1 * 3)

l1 = [1, 2]
l2 = [3, 4]

print("List Concatenation:", l1 + l2)
print("List Repetition:", l1 * 2)


#Comparison Operators (They are used to compare two values and return a boolean result):

x = 5
y = 10
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)


#Logical Operators (They are used to perform logical operations on boolean values):
y = True
z = False

print("Logical AND:", y and z)
print("Logical OR:", y or z)
print("Logical NOT:", not y)


#Assignment Operators (They are used to assign values to variables and can also perform an operation before assignment):

x1 = 5
x1 += 3 #This is equivalent to x1 = x1 + 3
print("After += operator:", x1)

x2 = 10
x2 *= 2 #This is equivalent to x2 = x2 * 2
print("After *= operator:", x2)

x3 = 20
x3 //= 4 #This is equivalent to x3 = x3 // 4 #// is floor division operator
print("After //= operator:", x3)

x4 = 15
x4 %= 4 #This is equivalent to x4 = x4 % 4
print("After %= operator:", x4)

x5 = 2
x5 **= 3 #This is equivalent to x5 = x5 ** 3
print("After **= operator:", x5)


#Bitwise Operators (They are used to perform bitwise operations on integers):
a1 = 5 # (0101)
b1 = 3 # (0011)

print("Bitwise AND:", a1 & b1) # (0001) (1 in decimal)
print("Bitwise OR:", a1 | b1) # (0111) (7 in decimal)
print("Bitwise XOR:", a1 ^ b1) # (0110) (6 in decimal)
print("Bitwise NOT:", ~a1) # (1010) (-6 in decimal)
print("Left Shift:", a1 << 1) # (1010) (10 in decimal)
print("Right Shift:", a1 >> 1) # (0010) (2 in decimal)


#Identity Operators (They are used to compare the memory locations of two objects):
x = 5
y = 5
z = [1, 2, 3]

print("is operator:", x is y) # True, as x and y refer to the same object
print("is not operator:", x is not y) # False, as x and y refer to the same object
print("is operator:", z is z) # True, as z refers to the same object


#Membership Operators (They are used to check if a value is present in a sequence or collection):
myList = [1, 2, 3, 4, 5]
print("in operator:", 3 in myList) # True, as 3 is in the list
print("not in operator:", 6 not in myList) # True, as 6 is not in the list


#Operator Precedence (It determines the order in which operators are evaluated in an expression):
result = 3 + 4 * 2
print("Result of 3 + 4 * 2:", result)
result = (3 + 4) * 2
print("Result of (3 + 4) * 2:", result)