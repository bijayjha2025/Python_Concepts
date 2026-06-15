
#Anything in between '', "", ''' ''', """ """ is a string in Python
a = 'Hello World'
b = "1234"
c = '''True'''
d = """2026-06-15"""
print(type(a), type(b), type(c), type(d)) #All these are of type string

#Python provides various built-in functions to manipulate strings.

# Case Conversion Methods: upper, lower, title, capitalize, swapcase, casefold
print("Hello Python World".upper())
print("Hello Python World".lower())
print("hello python world".title()) #Converts first character of each word to uppercase
print("hello python world".capitalize()) #Converts first character to uppercase
print("hELLO pYThon World".swapcase()) #Converts uppercase to lowercase and vice versa
print("Hello Python World".casefold()) #Converts string to lowercase for case-insensitive comparisons


#Searching Methods: find, rfind, index, rindex, count

s1 = "papaya"
print(s1.find('a')) #returns the index of first occurrence of 'a'
print(s1.find('x')) #returns -1 if 'x' is not found
print(s1.count('a')) #returns the number of occurrences of 'a'
print(s1.index('a')) #returns the index of first occurrence of 'a'
# print(s1.index('z')) #raises ValueError if 'z' is not found
print(s1.rfind('p')) #returns the index of last occurrence of 'p'
print(s1.rindex('p')) #returns the index of last occurrence of 'p' #rfind and rindex are similar but rindex raises ValueError if the substring is not found while rfind returns -1


#Testing/Validation Methods: isalpha, isdigit, isalnum, isspace, isnumeric, islower, isupper, isspace, istitle, isidentifier and all these return True or False based on the condition being checked

print("Hello".isalpha()) #True, all characters are alphabets
print("1234".isdigit()) #True, all characters are digits
print("Hello123".isalpha()) #False, contains both alphabets and digits
print("Hello123".isalnum()) #True, contains both alphabets and digits but no special characters
print("   ".isspace()) #True, all characters are whitespace
print("1234".isnumeric()) #True, all characters are numeric
print("hello".islower()) #True, all characters are lowercase
print("HELLO".isupper()) #True, all characters are uppercase
print("Hello World".istitle()) #True, first character of each word is uppercase
print("Hello World".isidentifier()) #False, contains space which is not allowed in identifiers
print("Hello_World".isidentifier()) #True, contains only letters, digits and underscores
print("Hello World".isprintable()) #True, all characters are printable
print("Hello\nWorld".isprintable()) #False, contains a newline character which is not printable


#Replace and modify methods: replace, strip, lstrip, rstrip, removeprefix, removesuffix

s2 = "   Hello World   "
print(s2.strip()) #removes leading and trailing whitespace
print(s2.lstrip()) #removes leading whitespace
print(s2.rstrip()) #removes trailing whitespace
print("Hello World".replace("World", "Python")) #replaces 'World' with 'Python'
print("Hello World".removeprefix("Hello ")) #removes the prefix 'Hello '
print("Hello World".removesuffix(" World")) #removes the suffix ' World'


#Splitting and Joining Methods: split, rsplit, splitlines, join

s = 'Java, Python, C++, C, Rust, Go, JS'
print(s.split(', ')) #splits the string into a list based on the delimiter ', '
print(s.rsplit(', ', 2)) #splits the string into a list based on the delimiter ', ' from the right, with a maximum of 1 split

