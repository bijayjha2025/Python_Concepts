# Use for loop to print each country in the countries list.

countriesList = ['USA', 'Canada', 'Germany', 'France', 'Japan']
for country in countriesList:
    print(country.upper())

# Use map to create a new list by changing each country to uppercase in the countries list
capitalizedCountries = list(map(str.upper, countriesList))
print(capitalizedCountries)

# Use for to print each name in the names list.
for name in ['Chetan', 'Khoi', 'Rahul']:
    print(name.upper())


# Use map to change each name to uppercase in the names list
capitalizedNames = list(map(str.upper, ['Chetan', 'Khoi', 'Rahul']))
print(capitalizedNames)

# Use for to print each number in the numbers list.
for number in [1, 2, 3, 4, 5]:
    print(number)


# Use map to create a new list by changing each number to its square in the numbers list
squaredNumbers = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squaredNumbers)


nations = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Nepal', 'Thailand', 'Ireland', 'Poland', 'Switzerland']
# Use filter to filter out countries containing 'land'.

def filterCountries(country):
    return 'land' in country

filteredCountries = list(filter(filterCountries, nations))
print(filteredCountries)

# Use filter to filter out countries having exactly six characters.

def filterSixCharCountries(country):
    return len(country) == 6

filteredSixCharCountries = list(filter(filterSixCharCountries, nations))
print(filteredSixCharCountries)

# Use filter to filter out countries containing six letters and more in the country list.

def filterSixOrMoreCharCountries(country):
    return len(country) >= 6

filteredSixOrMoreCharCountries = list(filter(filterSixOrMoreCharCountries, nations))
print(filteredSixOrMoreCharCountries)


def filterExactFive(country):
    return len(country) == 5

withFiveCharCountries = list(filter(filterExactFive, nations))
print(withFiveCharCountries)


# Use filter to filter out countries starting with an 'E'

def startsWithE(country):
    return country.startswith('E')

eCountries = list(filter(startsWithE, nations))
print(eCountries)

