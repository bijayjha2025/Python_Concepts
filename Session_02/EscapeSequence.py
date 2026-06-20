"""
Escape sequences: They are special characters that are not printed but are used to represent certain characters or perform specific actions in a string. They are denoted by a backslash (\) followed by a character that represents the escape sequence.

Common Escape Sequences: \n, \t, \\, \', \", \b
"""

print("Hello\nWorld") #This will print "Hello" and "World" on separate lines
print("Hello\tWorld") #This will print "Hello" and "World" separated by a tab space
print("This is a backslash: \\ ") #This will print a single backslash
print("This is a single quote: \' ") #This will print a single quote
print("This is a double quote: \" ") #This will print a double quote
print("Hello\bWorld") #This will print "HellWorld" because the backspace will remove the last character "o" from "Hello"