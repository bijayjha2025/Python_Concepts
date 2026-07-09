'''
Syntax to open file: open('filename', 'mode')
'r'=Read mode (default)
'w'=Write mode
'a'=Append mode
'x'= create mode
'r+'=Read and Write mode
't'=Text mode (default)
'b'=Binary mode


'''

#Example of reading a file
file = open('./Session_08/files/test.txt')
text = file.read()
print(text)
print(type(text))
file.close()

#Instead of printing whole text, we can read first few characters
file = open('./Session_08/files/test.txt')
text = file.read(10)
print(text)
print(type(text))
file.close()

#readline() method is used to read a single line from the file
file = open('./Session_08/files/test.txt')
line1 = file.readline()
print(line1, type(line1))
line2 = file.readline()
print(line2, type(line2))
file.close()


#readlines() method is used to read all the lines from the file and return them as a list of strings
file = open('./Session_08/files/test.txt')
lines = file.readlines()
print(lines, type(lines))
file.close()

#Another way to get all lines is splitlines
file = open('./Session_08/files/test.txt')
linesall = file.read().splitlines()
print(linesall, type(linesall))
file.close()


#Opening files for writing and updating
with open('./Session_08/files/test1.txt', 'w') as file: #with automatically closes the file
    file.write("This is a new line in the file.") #if not, it will create
    file.write("\nThis is another line in the file.")
    file.write("\nThis is yet another line in the file.")

with open('./Session_08/files/test.txt', 'a') as file:
    file.write("\nThis line is appended to the file.")
    file.write("\nThis is another appended line.")

#Deleting a file
#If the file does not exist, it will raise a FileNotFoundError, so its better to check if the file exists before deleting it

import os
if os.path.exists('./Session_08/files/del.txt'):
    os.remove('./Session_08/files/del.txt')
    print("File deleted successfully.")
else:
    print("File does not exist.")
