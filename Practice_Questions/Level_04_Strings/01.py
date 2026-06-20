# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'

concat = str1 + " " + str2 + " " + str3 + " " + str4
print(concat)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

str5 = "Coding"
str6 = "For"
str7 = "All"

concat2 = str5 + " " + str6 + " " + str7
print(concat2)


# Declare a variable named company and assign it to an initial value "Coding For All".

company = '''Coding For All'''
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut (slice) out the first word of the string 'Coding For All' and store it in a variable named first_word.

firstWord = company[0:6]
print(firstWord)

# Check if the string 'Coding For All' contains a word 'Coding'.
print(company.find("Coding"))

# Replace the word 'Coding' with 'Python' and print out the result.
print(company.replace('Coding', "Python"))

# Split the string 'Coding For All' using space as the separator (split()) and print out the result.

print(company.split(" "))
