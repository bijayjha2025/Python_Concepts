'''
Function: It is a reusable block of code or programming statements designed to perform a specific task. To declare a function, we use the def keyword followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented. Functions can take inputs, called parameters, and can return outputs using the return statement. The function code is only executed when the function is called. Functions help in breaking our program into smaller and modular chunks, making it more organized and manageable.

Syntax
def function_name():
    # code block
    
function_name()
'''

# Function can be declared without parameters and without return value
def greet():
    print("Hello, welcome to the world of functions!")

greet()
greet()  # Calling the function to execute its code block



def generate_fullName():
    firstName = "Bijay"
    lastName = "Okay"
    fullName = firstName + " " + lastName
    print(fullName)


generate_fullName()  # Calling the function to execute its code block


def add_numbers():
    num1 = 5
    num2 = 10
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum)

add_numbers()  # Calling the function to execute its code block


# Function returning value
def multiplyNumbers():
    num1 = 5
    num2 = 10
    product = num1 * num2
    return product

result = multiplyNumbers()  # Calling the function and storing the returned value
print("The product of 5 and 10 is:", result) #Note that to print the returned value, we need to call the function and store its return value in a variable, which can then be printed.


#Function with parameters
def greetUser(name):
    print("Hello,", name, "! Welcome to the world of functions!")

greetUser("Bijay")  # Calling the function with an argument


# A function can have multiple parameters
def addNumbers(num1, num2):
    sum = num1 + num2
    return sum

result = addNumbers(5, 10)  # Calling the function with two arguments and storing the returned value
print("The sum of 5 and 10 is:", result)  # Printing the returned value

#What is the difference between a parameter and an argument in a function?
# A parameter is a variable that is defined in the function declaration and acts as a placeholder for the value that will be passed to the function when it is called. An argument, on the other hand, is the actual value that is passed to the function when it is called. In other words, parameters are used in the function definition, while arguments are used in the function call. Other than that, parameters are used to define the input of a function, while arguments are used to provide the actual input values when calling the function.


# Passing arguments with key and value
def greetUser(name, age):
    print("Hello,", name, "! You are", age, "years old.")

greetUser(name="Bijay", age=20)  # Calling the function with keyword arguments

#Default parameter values: When defining a function, we can assign default values to parameters. If the caller does not provide a value for that parameter, the default value will be used. This allows us to create functions that can be called with varying numbers of arguments.
def greetUser(name, age=18):
    print("Hello,", name, "! You are", age, "years old.")

greetUser(name="Bijay")  # Calling the function with only the name argument, age will take the default value of 18