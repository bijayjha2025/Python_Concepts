# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(inputArray):
    reversedArray = []
    for i in range(len(inputArray) - 1, -1, -1):
        reversedArray.append(inputArray[i])
    return reversedArray

result = reverse_list([1, 2, 3, 4, 5])
print(f"The reverse of the array [1, 2, 3, 4, 5] is: {result}")

result2 = reverse_list(['a', 'b', 'c', 'd'])
print(f"The reverse of the array ['a', 'b', 'c', 'd'] is: {result2}")


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(inputList):
    capitalizedList = []
    for item in inputList:
        capitalizedList.append(item.capitalize())
    return capitalizedList

result3 = capitalize_list_items(['hello', 'world'])
print(f"The capitalized list of items ['hello', 'world'] is: {result3}")


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(inputList, item):
    inputList.append(item)
    return inputList

result4 = add_item([1, 2, 3], 4)
print(f"The list after adding the item 4 to [1, 2, 3] is: {result4}")


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(inputList, item):
    if item in inputList:
        inputList.remove(item)
    return inputList

result5 = remove_item([1, 2, 3, 4], 3)
print(f"The list after removing the item 3 from [1, 2, 3, 4] is: {result5}")


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result6 = sum_of_numbers(5)
print(f"The sum of numbers from 1 to 5 is: {result6}")


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i
    return total

result7 = sum_of_odds(5)
print(f"The sum of odd numbers from 1 to 5 is: {result7}")


# Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

result8 = sum_of_evens(5)
print(f"The sum of even numbers from 1 to 5 is: {result8}")