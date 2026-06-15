#In Python, a string is anything that is enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

name = "Okay"
name2 = "o"
name3 = "120"
name4 = "True"
name5 = "2020-01-01"

print(type(name))
print(type(name2))
print(type(name3))
print(type(name4))
print(type(name5)) #All these are strings, even though they may look like numbers or boolean values.


#String built-in functions: Python has several built-in functions that can be used to manipulate strings.

#len() => This function returns the length of a string. general syntax: len(string)
print(len(name))
print(len(name2))
print(len(name3))
print(len(name5))

# 1. Case Modification Functions:
#a. lower() => This converts all the characters in a string to lowercase. general syntax: string.lower()
print(name.lower())
print(name5.lower())
print(name4.lower())

# b. upper() => This converts all the characters in a string to uppercase. general syntax: string.upper()
print(name.upper())
print(name4.upper())

# c. capitalize() => This converts the first character of a string to uppercase and the rest to lowercase. general syntax: string.capitalize()
test = "hello world"
print(test.capitalize())

# d. title() => This capitalizes the first character of each word in a string. general syntax: string.title()
testA = "hello world, i am learning python programming."
print(testA.title())

# e. swapcase() => This converts uppercase characters to lowercase and lowercase characters to uppercase in a string. general syntax: string.swapcase()
testB = "Hello World"
print(testB.swapcase())


# 2. Searching and Counting Functions:

# a. find() => This returns the index of the first occurrence of a specified substring in a string. general syntax: string.find(substring)

string = "Psychology is the scientific study of the mind and behavior."

print(string.find("World")) #returns the index of the first occurrence of "World"
print(string.find("Python")) #returns -1 if the substring is not found

# b. rfind() => This returns the index of the last occurrence of a specified substring in a string. general syntax: string.rfind(substring)
print(string.rfind("the")) #returns the index of the last occurrence of "the"


# c. count() => This returns the number of occurrences of a specified substring in a string. general syntax: string.count(substring)
print(string.count("o")) #returns the number of occurrences of "o" in the string
print(string.count("l")) #returns the number of occurrences of "l" in the string

# d. string indexing => This allows us to access individual characters in a string using their index. general syntax: string[index]

string = "Hello World"
print(string[0]) #accessing the first character
print(string[6]) #accessing the seventh character
print(string[-1]) #accessing the last character
print(string[-6]) #accessing the sixth character from the end
print(string[0:5]) #accessing a substring from index 0 to 4
print(string[6:11]) #accessing a substring from index 6 to 10
print(string[:5]) #accessing a substring from the beginning to index 4
print(string[6:]) #accessing a substring from index 6 to the end

# e. startswith() => This checks if a string starts with a specified substring. general syntax: string.startswith(substring)
print(string.startswith("Hello")) #returns True if the string starts with "Hello"
print(string.startswith("World")) #returns False if the string does not start with "World"

# f. endswith() => This checks if a string ends with a specified substring. general syntax: string.endswith(substring)
print(string.endswith("World")) #returns True if the string ends with "World"
print(string.endswith("Hello")) #returns False if the string does not end with "Hello"

# g. isalpha() => This checks if all characters in a string are alphabetic. general syntax: string.isalpha()
print(name.isalpha()) #returns True if all characters in the string are alphabetic

name6 = "Hello123"
print(name6.isalpha()) #returns False if there are any non-alphabetic characters in the string


# 3. Cleaning and modifying functions:
# a. strip() => This removes any leading and trailing whitespace from a string. general syntax: string.strip()
test2 = "   Hello World   "
print(test2)
print(test2.strip())

# b. lstrip() => This removes any leading whitespace from a string. general syntax: string.lstrip()
print(test2.lstrip())

# c. rstrip() => This removes any trailing whitespace from a string. general syntax: string.rstrip()
print(test2.rstrip())


# d. replace() => This replaces a specified substring with another substring in a string. general syntax: string.replace(old, new)

test3 = "Hello World"
print(test3.replace("World", "Class 12"))

# e. removeprefix() => This removes a specified prefix from the beginning of a string. general syntax: string.removeprefix(prefix)
test4 = "Hello World"
print(test4.removeprefix("Hello ")) #removes "Hello " from the beginning of the string

# f. removesuffix() => This removes a specified suffix from the end of a string. general syntax: string.removesuffix(suffix)
test5 = "Hello World"
print(test5.removesuffix(" World")) #removes " World" from the end of the string

# 4. Splitting and joining

#concatenation => This is the process of combining two or more strings together. general syntax: string1 + string2

firstName = "Bijay"
lastName = "Jha"
fullName = firstName + " " + lastName
print(fullName)


#Concatenation can also be done using the join() method. general syntax: "separator".join(iterable)
firstName = "Haha"
secondName = "Hehe"
fullname2 = " ".join([firstName, secondName])
print(fullname2)


#split() => This splits a string into a list of substrings based on a specified delimiter. general syntax: string.split(separator)
sentence = "Hello World, welcome to Python programming."
print(sentence.split()) #splits the sentence into a list of words using space as the delimiter
print(sentence.split(",")) #splits the sentence into a list of substrings using comma as the delimiter




#string formatting => This allows us to insert values into a string using placeholders. general syntax: "string with placeholders".format(values)
age = 23
print("My name is {} and I am {} years old.".format(fullName, age))





