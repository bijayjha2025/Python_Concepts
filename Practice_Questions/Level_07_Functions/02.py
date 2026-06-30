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