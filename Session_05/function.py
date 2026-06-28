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