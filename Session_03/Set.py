'''
Set => Set refers to a collection of unique elements. It is an unordered collection, meaning that the elements do not have a specific order. Sets are mutable, which means that we can add or remove elements from a set after it has been created. However, the elements themselves must be immutable (e.g., numbers, strings, tuples). Sets are defined using curly braces {} or the set() constructor. The items in a set can be of different data types (e.g., integers, strings, floats, etc.). Note that for strings in a set, we need to enclose them in quotes (either single or double) whereas for other data types, we can directly write them without quotes.
'''

mySet = {1, 2, 3, 4, 5} #set of integers
mySet2 = {"apple", "banana", "cherry"} #set of strings
mySet3 = {1, "apple", 3.14, True} #set of mixed data types
print(f"{mySet}: {type(mySet)}\n{mySet2}: {type(mySet2)}\n{mySet3}: {type(mySet3)}")

# Set methods: add, update, remove, discard, pop, clear, union, intersection, difference, symmetric_difference
mySet.add(6) #adds 6 to the set
print(mySet)
mySet.update([7, 8, 9]) #adds multiple items to the set
print(mySet)
mySet.remove(5) #removes 5 from the set, raises a KeyError if 5 is not found
print(mySet)
mySet.discard(4) #removes 4 from the set, does not raise an error if 4 is not found
print(mySet)
mySet.pop() #removes and returns an arbitrary element from the set, raises a KeyError if the set is empty
print(mySet)
mySet.clear() #removes all items from the set
print(mySet)
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(setA.union(setB)) #returns a new set that contains all the elements from both sets
print(setA.intersection(setB)) #returns a new set that contains only the elements that are common to both sets
print(setA.difference(setB)) #returns a new set that contains the elements that are in setA but not in setB
print(setA.symmetric_difference(setB)) #returns a new set that contains the elements that are in either setA or setB but not in both sets
print(setA)