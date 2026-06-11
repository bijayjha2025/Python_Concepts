'''
Variables => It is a name that refers to a value stored in memory. Remember it as a container that holds data. Note that it does not hold a value but rather a reference to the value. In Python, variables are created when you assign a value to them. The variable name can be any valid identifier, and it can hold values of different data types such as integers, floats, strings, lists, etc. Variables in Python are dynamically typed, which means you can change the type of value a variable holds without declaring it explicitly. For example, you can assign an integer to a variable and later assign a string to the same variable without any issues. This flexibility allows for more dynamic and versatile programming in Python.
'''

x = 10
print(x)
x = "Hello"
print(x)
x = [1, 2, 3]
print(x)

#In above example, we first assign the integer value 10 to the variable x, then we reassign it to a string "Hello", and finally to a list [1, 2, 3]. This demonstrates the dynamic typing feature of Python variables.

'''
Rules for Variable Names:
a. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
b. Variable names can contain letters, digits (0-9), and underscores, but cannot start with a digit.
c. Variable names are case-sensitive, which means that 'variable1' and 'Variable1' are considered different variables.
d. Variable names cannot be the same as Python reserved keywords (like 'if', 'for', 'while', etc.).
e. Variable names should be descriptive and meaningful to improve code readability.
f. Variable names should not contain spaces. Instead, you can use underscores to separate words (e.g., 'my_variable').
g. Variable names should not start with a double underscore (__) as it is reserved for special methods in Python.
'''

#Examples of valid variable names
my_variable = 10
_variable = "Hello"
variable1 = [1, 2, 3]

#Examples of invalid variable names
#1variable = 10 #Invalid because it starts with a digit
#my variable = "Hello" #Invalid because it contains a space
#for = 5 #Invalid because 'for' is a reserved keyword in Python
#__my_variable = 10 #Invalid because it starts with a double underscore
#variable-name = "Hello" #Invalid because it contains a hyphen


#Variable Assignment => In Python, we can assign values to variables using the assignment operator (=) and it is possible to perform multiple assignments in a single line. For example:
a, b, c = 7, 8, 9
print(a, b, c)

p, q, r = "Orange", "Apple", "Papaya"
print(p, q, r)
print(p)
print(q)
print(r)

#To add one value to more than one variable, we can use the following syntax:
x1 = x2 = x3 = "Banana"
print(x1, x2, x3)

#Variable Reassignment => In Python, we can reassign a variable to a new value at any time. When we reassign a variable, it simply points to the new value in memory, and the old value may be garbage collected if there are no other references to it. For example:
x = 10
print(x) # Output: 10
x = 20
print(x) # Output: 20


t1 = "10"
t2 = "Alpha"

print(t1, t2)
print(t1 + t2)


'''
Types of variables:
a. Local Variables: These are variables that are defined within a function and can only be accessed within that function. They are created when the function is called and destroyed when the function exits.
b. Global Variables: These are variables that are defined outside of any function and can be accessed from anywhere in the code. They are created when the program starts and destroyed when the program ends.
'''

var = 10

def add():
    print("Inside function")
    print(var)

add()
print(var)

#Here var is a global variable because it is defined outside the function and can be accessed both inside and outside the function.


def anotherfunction():
    varNew = 20
    print("Inside another function")
    print(varNew)

anotherfunction()
print(varNew) #This will raise an error because varNew is a local variable and cannot be accessed outside the function where it is defined.


#There is a fun thing you can try. You can use the global keyword to modify a global variable inside a function. For example:

def thirdFunction():
    global varthird
    varthird = 30
    print("Inside third function")
    print(varthird)

thirdFunction()
print(varthird) #This will work because we declared varthird as a global variable inside the function using the global keyword, allowing us to access and modify it outside the function as well.
