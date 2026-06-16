'''
Dictionary => It is a data structure that stores data in key-value pairs. It is unordered, changeable, and does not allow duplicate keys. The data items are enclosed in curly braces {} and separated by commas. Each key is separated from its value by a colon (:). The items in a dictionary can be of different data types (e.g., integers, strings, floats, etc.). Note that for strings in a dictionary, we need to enclose them in quotes (either single or double) whereas for other data types, we can directly write them without quotes.
'''

myDictionary = {
    "name": "Bijay",
    "subject": "CS",
    "address": "Itahari",
    "isStudent": True,
    "marks": [85, 90, 95],
}

print(f"{myDictionary}: {type(myDictionary)}")

# Dictionary methods: keys, values, items, get, pop, popitem, clear, update
print(myDictionary.keys()) #returns a view object that displays a list of all the keys in the dictionary
print(myDictionary.values()) #returns a view object that displays a list of all the values in the dictionary
print(myDictionary.items()) #returns a view object that displays a list of all the key-value pairs in the dictionary as tuples
print(myDictionary.get("name")) #returns the value associated with the key "name" in the dictionary
print(myDictionary.pop("address")) #removes the key "address" and its associated value from the dictionary and returns the value
print(myDictionary.popitem()) #removes and returns the last key-value pair added to the dictionary as a tuple
print(myDictionary)
myDictionary.clear() #removes all items from the dictionary
print(myDictionary)
myDictionary.update({"name": "Bijay", "subject": "CS", "address": "Itahari", "isStudent": True, "marks": [85, 90, 95]}) #updates the dictionary with the key-value pairs from another dictionary
print(myDictionary)
