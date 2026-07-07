# '''
# Exception Handling in Python
# Python uses exception handling to manage errors that occur during the execution of a program. It allows us to catch and handle exceptions gracefully, preventing the program from crashing. The main components of exception handling in Python are:
# 1. try block: This is the block of code where we write the code that may raise an exception. We use the try block to enclose the code that we want to monitor for exceptions.
# 2. except block: This is the block of code that is executed if an exception occurs in the try block. We can specify the type of exception we want to catch, or we can catch all exceptions using a generic except block.
# 3. else block: This is an optional block that is executed if no exceptions occur in the try block. It is used to define code that should run only if the try block was successful.
# 4. finally block: This is an optional block that is executed regardless of whether an exception occurred or not. It is used to define code that should always run, such as cleanup operations or closing resources.

# '''

# try:
#     print(10+"5")

# except:
#     print('Something went wrong. Please check your code.')


# try:
#     name = input("Enter your name: ")
#     birthYear = int(input("You were born in which year? "))
#     age = 2026 - birthYear
#     print(f"Your age is: {age} and you are {name}")

# except:
#     print("Invalid input. Please enter a valid year.")


# #In this example, we will look at different kinds of errors and handle them.

# try:
#     name = input("Enter your name: ")
#     yearBorn = int(input("You were born in which year? "))
#     age = 2026 - yearBorn
#     print(f"Your age is: {age} and you are {name}")

# except ValueError:
#     print("Value Error: Invalid input. Please enter a valid year.")

# except TypeError:
#     print("Type Error: Invalid input type. Please enter a valid year.")

# except ZeroDivisionError:
#     print("Zero Division Error.")



try:
    address = input("Enter your address: ")
    yearBorn = int(input("You were born in which year? "))
    age = 2026 - yearBorn
    print(f"Your age is: {age} and you are {name} and your address is {address}")

except ValueError:
    print("Value Error: Invalid input. Please enter a valid year.")

except TypeError:
    print("Type Error: Invalid input type. Please enter a valid year.")

except ZeroDivisionError:
    print("Zero Division Error.")


else:
    print("No errors occurred. The program executed successfully.")

finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")