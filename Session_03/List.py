'''
List => It is a collection of items which are ordered and changeable. It allows duplicate members. The data items are enclosed in square brackets [] and separated by commas. The items in a list can be of different data types (e.g., integers, strings, floats, etc.). Note that for strings in a list, we need to enclose them in quotes (either single or double) whereas for other data types, we can directly write them without quotes.
'''

list1 = [1, 2, 3, 4, 5] #list of integers
list2 = ["apple", "banana", "cherry"] #list of strings
list3 = [1, "apple", 3.14, True] #list of mixed data types
print(f"{list1}: {type(list1)}\n{list2}: {type(list2)}\n{list3}: {type(list3)}")

# List methods: append, extend, insert, remove, pop, clear, index, count, sort, reverse
list1.append(6) #adds 6 to the end of the list
print(list1)

list1.extend([7, 8, 9]) #adds multiple items to the end of the list
print(list1)

list1.insert(0, 0) #two parameters: index and value, inserts 0 at index 0, and all other elements are shifted to the right
print(list1)

list1.remove(5) #removes the first occurrence of 5 from the list
print(list1)

list1.pop() #removes and returns the last item from the list
print(list1)

list1.index(3) #returns the index of the first occurrence of 3 in the list
print(list1.index(3))

list1.count(3) #returns the number of occurrences of 3 in the list
print(list1.count(3))

list1.sort() #sorts the list in ascending order
print(list1)

list1.reverse() #reverses the order of the list
print(list1)


list1.clear() #removes all items from the list
print(list1)

list4 = [3, 1, 4, 1, 5, 9]
print(list4)

