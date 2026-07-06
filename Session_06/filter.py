#Filter method is used to filter the elements of an iterable (like a list, tuple, or set) based on a function that returns either True or False. The filter() function takes two arguments: a function and an iterable. It applies the function to each element of the iterable and returns an iterator that contains only the elements for which the function returned True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(num):
    if num % 2 == 0:
        return True
    return False

evenNumbers = list(filter(isEven, numbers))
print(evenNumbers)

def isOdd(num):
    if num % 2 != 0:
        return True
    return False

oddNumbers = list(filter(isOdd, numbers))
print(oddNumbers)

#filter long names
names = ["Magesh", "Max", "Karl", "Bill", "John", "Alexandra", "Elizabeth"]

def isLongName(name):
    if len(name) > 5:
        return True
    return False

longNames = list(filter(isLongName, names))
print(longNames)

#Another example using lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda num: num % 2 == 0, numbers))
print(evenNumbers)