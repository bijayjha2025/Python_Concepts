'''
String Slicing => It is a technique to extract a portion of a string by specifying the start and end indices. The syntax for slicing is: string[start:end:step]. The start index is inclusive, while the end index is exclusive. The step parameter is optional and specifies the increment between each index.
'''

string = "PYTHON"
print(string[0:4]) #returns characters from index 0 to 3 (before reaching index 4)
print(string[2:5]) #returns characters from index 2 to 4 (before reaching index 5)
print(string[1:4]) #returns characters from index 1 to 3 (before reaching index 4)
print(string[:3]) #returns characters from the beginning of the string to index 2 (before reaching index 3)
print(string[3:6]) #returns characters from index 3 to 5 (before reaching index 6)

print(string[-2:]) #returns the last two characters of the string
print(string[:-2]) #returns the string without the last two characters

print(string[::2]) #returns every second character of the string
print(string[1::2]) #returns every second character of the string starting from index 1
print(string[::-1]) #returns the string in reverse order

print(string[1:5:2]) #returns characters from index 1 to 4 (before reaching index 5) with a step of 2
print(string[5:1:-1]) #returns characters from index 5 to 2 (before reaching index 1) in reverse order
print(string[5:1:-2]) #returns characters from index 5 to 2 (before reaching index 1) in reverse order with a step of 2
print(string[1:5:-1]) #returns an empty string because the step is negative and the start index is less than the end index
print(string[5:1:1]) #returns an empty string because the step is positive and the start index is greater than the end index

print(string[1:5:0]) #raises ValueError because the step cannot be zero

print(string[1:5:]) #returns characters from index 1 to 4 (before reaching index 5) with a default step of 1