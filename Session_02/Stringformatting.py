'''
Python supports various ways of formatting strings, which allow us to create dynamic and formatted output. Here are some common methods for string formatting in Python:
f-strings(formatted string literals)
% formatting
str.format() method
'''

#1. % formatting: This is an older method of string formatting that uses the % operator to format strings. It is similar to printf-style formatting in C.

name = "Bijay"
age = 20
subject = "CS"

print("My name is %s, I am %d years old and I teach %s to Grade 10 students." %(name, age, subject))

# %s is used for string formatting, %d is used for integer formatting, and %f is used for floating-point formatting. We can also specify the width and precision of the formatted output using the format specifiers. For example, %.2f will format a floating-point number to 2 decimal places.


# 2. str.format() method: This is a more modern method of string formatting that uses the format() method of strings. It allows us to use placeholders in the string and replace them with values.


nameNew = "Bijay"
ageNew = 20
subjectNew = "CS"

print("My name is {}, I am {} years old and I teach {} to Grade 10 students.".format(nameNew, ageNew, subjectNew))

# We can also use positional or keyword arguments in the format() method to specify the order of the values. For example, {0} will refer to the first argument, {1} will refer to the second argument, and so on. We can also use named placeholders like {name} and {age} and pass the values as keyword arguments to the format() method.

list = ["Bijay", 20, "CS"]
print("My name is {0}, I am {1} years old and I teach {2} to Grade 10 students.".format(list[0], list[1], list[2]))


# 3. f-strings (formatted string literals): This is the most modern and recommended method of string formatting in Python. It allows us to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and the resulting values are formatted and inserted into the string.


firstName = "Bijay"
surname = "Jha"
subjectF = "CS"

print(f"My name is {firstName} {surname}, I teach {subjectF} to Grade 10 students.")

# We can also include expressions inside the curly braces, such as calculations or function calls. For example, {age + 5} will evaluate the expression age + 5 and insert the result into the string.


list3 = ["Bijay", 20, "CS"]
print(f"My name is {list3[0]}, I am {list3[1] + 2} years old and I teach {list3[2]} to Grade 10 students.")