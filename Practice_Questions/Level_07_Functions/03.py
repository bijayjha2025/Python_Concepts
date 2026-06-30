
# Function to check whether a number is prime or not

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

result8 = isPrime(7)
print(f"Is 7 a prime number? {result8}")

result9 = isPrime(10)
print(f"Is 10 a prime number? {result9}")


# Write a functions which checks if all items are unique in the list.

def checkUnique(inputList):
    return len(inputList) == len(set(inputList))

result10 = checkUnique([1, 2, 3, 4])
print(f"Are all items in the list [1, 2, 3, 4] unique? {result10}")


# Write a function which checks if all the items of the list are of the same data type.

def checkSameDataType(inputList):
    if not inputList:
        return True  # An empty list is considered to have the same data type
    first_type = type(inputList[0])
    for item in inputList:
        if type(item) != first_type:
            return False
    return True

result11 = checkSameDataType([1, 2, 3, 4])
print(f"Are all items in the list [1, 2, 3, 4] of the same data type? {result11}")



# Write a function which check if provided variable is a valid python variable

def isValidVariableName(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

result12 = isValidVariableName("myVariable")
print(f"Is 'myVariable' a valid Python variable name? {result12}")


# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order


def most_spoken_languages():
    languages = {
        'English': 1132,
        'Mandarin Chinese': 1117,
        'Hindi': 615,
        'Spanish': 534,
        'French': 280,
        'Arabic': 274,
        'Bengali': 265,
        'Russian': 258,
        'Portuguese': 234,
        'Indonesian': 199
    }
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return [language[0] for language in sorted_languages]

result13 = most_spoken_languages()
print(f"The most spoken languages in the world are: {result13}")



# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def most_populated_countries():
    countries = {
        'China': 1444216107,
        'India': 1393409038,
        'United States': 331893745,
        'Indonesia': 273523621,
        'Pakistan': 220892331,
        'Brazil': 212559409,
        'Nigeria': 206139587,
        'Bangladesh': 164689383,
        'Russia': 145912025,
        'Mexico': 128932753
    }
    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    return [country[0] for country in sorted_countries]

result14 = most_populated_countries()
print(f"The most populated countries in the world are: {result14}")