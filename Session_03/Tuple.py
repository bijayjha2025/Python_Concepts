'''
Tuple => It is a collection of items which are ordered and unchangeable. It allows duplicate members. The data items are enclosed in parentheses () and separated by commas. The items in a tuple can be of different data types (e.g., integers, strings, floats, etc.). Note that for strings in a tuple, we need to enclose them in quotes (either single or double) whereas for other data types, we can directly write them without quotes.
'''

myTuple = (1, 2, 3, 4, 5) #tuple of integers
myTuple2 = ("apple", "banana", "cherry") #tuple of strings
myTuple3 = (1, "apple", 3.14, True) #tuple of mixed data types
print(f"{myTuple}: {type(myTuple)}\n{myTuple2}: {type(myTuple2)}\n{myTuple3}: {type(myTuple3)}")

# Tuple methods: count, index
myTuple.count(3) #returns the number of occurrences of 3 in the tuple
print(myTuple.count(3))

myTuple.index(3) #returns the index of the first occurrence of 3 in the tuple
print(myTuple.index(3))

# Tuples are immutable, which means we cannot change their values after they are created. However, we can convert a tuple to a list, modify the list, and then convert it back to a tuple if needed.
myList = list(myTuple) #converts the tuple to a list
print(myList, type(myList))

myList.append(6) #modifies the list by adding 6 to the end of it
print(myList)

myTuple = tuple(myList) #converts the modified list back to a tuple
print(myTuple, type(myTuple))

#In Tuple, we can also find maximum and minimum values using max() and min() functions respectively.
print(max(myTuple)) #returns the maximum value in the tuple
print(min(myTuple)) #returns the minimum value in the tuple

print(sum(myTuple)) #returns the sum of all the values in the tuple
print(sorted(myTuple)) #returns a sorted list of the values in the tuple



#Nested Tuple => A tuple that contains another tuple as an item is called a nested tuple. We can access the values in a nested tuple by using multiple indices.
nestedTuple = (1, 2, (3, 4), 5) #tuple that contains another tuple as an item
print(nestedTuple[2]) #accesses the nested tuple (3, 4)

print(nestedTuple[2][0]) #accesses the first item (3) in the nested tuple (3, 4)
print(nestedTuple[2][1]) #accesses the second item (4) in the nested tuple (3, 4)
print(nestedTuple[2][0] + nestedTuple[2][1]) #adds the first and second items in the nested tuple (3 + 4 = 7)