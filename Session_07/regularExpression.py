'''
Regular Expression
It refers to a sequence of characters that forms a search pattern. It is used for pattern matching and manipulation of strings. Regular expressions are widely used in programming languages, text editors, and command-line tools for tasks such as searching, replacing, and validating text.

re module: In Python, the re module provides support for working with regular expressions. It allows us to search for patterns in strings, extract information, and perform various operations on text data.
Various functions provided by the re module include:
a. re.match(): This function checks for a match only at the beginning of the string. Syntax: re.match(pattern, string, flags=0)
b. re.search(): This function searches for a match anywhere in the string. Syntax: re.search(pattern, string, flags=0)
c. re.findall(): This function returns a list of all non-overlapping matches of the pattern in the string. Syntax: re.findall(pattern, string, flags=0)
d. re.sub(): This function replaces occurrences of the pattern in the string with a specified replacement string. Syntax: re.sub(pattern, repl, string, count=0, flags=0)
e. re.split(): This function splits the string by occurrences of the pattern. Syntax: re.split(pattern, string, maxsplit=0, flags=0)
'''

import re

txt = "Itahari is a city in eastern Nepal"

match = re.match("Itahari", txt)
print(match) #Using match() function to check if the string starts with "Itahari"

span = match.span()
print(span) #Using span(), we can get the start and end positions of the match in the string in the form of a tuple (start, end)

start, end = span
print(start, end) #Using unpacking, we can assign the start and end positions to separate variables

substring = txt[start:end]
print(substring) #Using the start and end positions, we can extract the matched substring from the original string

search = re.search("city", txt)
print(search) #Using search(), we can check if the string contains the word "city"


#Searching for all occurrences of a pattern in a string using findall()

newText = "Python is an exciting language to learn and python has got many advantages. This language is easy to learn and has a simple syntax. Python is also a versatile language that can be used for web development, data analysis, machine learning, and more. Language is a powerful tool for solving problems and creating innovative solutions. Learning a new language can be challenging, but it can also be rewarding and fun. With dedication and practice, anyone can become proficient in a new language and open up new opportunities for personal and professional growth."
matches = re.findall("language", newText)
print(matches) #Using findall(), we can get a list of all occurrences of the word "language" in the string


matches = re.findall("language", newText, re.I) #with this, it will ignore the case of the pattern and match "language" regardless of its case (e.g., "Language", "LANGUAGE", etc.)
print(matches) #Using findall(), we can get a list of all occurrences of the word


#Replacing 
matchReplace = re.sub('Python|python', 'Javascript', newText) #Using sub(), we can replace all occurrences of the word "Python" or "python" with "JavaScript"
print(matchReplace) #Using sub(), we can replace all occurrences of the word "Python"


#Splitting using split()
splitText = re.split('language', newText) #Using split(), we can split the string into a list of substrings based on the occurrences of the word "language"
print(splitText) #Using split(), we can split the string into a list of substrings