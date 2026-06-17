'''
Conditional Statements => It is used to perform different actions based on different conditions. It is also known as decision making statements. In Python, we have the following conditional statements:
1. if statement
2. if-else statement
3. if-elif-else statement
'''

# if statement: we use this to execute a block of code if a specified condition is true. If the condition is false, the block of code will be skipped.

age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")


# if-else statement: we use this to execute a block of code if a specified condition is true, and another block of code if the condition is false.

age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")


# if-elif-else statement: we use this to execute a block of code if a specified condition is true, and another block of code if the condition is false, and another block of code if the condition is false.

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

else:
    print("The number is zero.")


# In such cases, the conditions are evaluated from top to bottom, and the first true condition is executed. If none of the conditions are true, the else block is executed.


#While doing conditional statments, pay attention to the indentation. In Python, indentation is used to define the scope of loops, functions, and other code blocks. If the indentation is not correct, it will lead to a syntax error.