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