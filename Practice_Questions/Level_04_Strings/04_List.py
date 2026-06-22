
listE = [] # Initializing an empty list

listB = [1, "Bijay", 3.14, 2, True, 6700] # List with mixed data types

print(f"{listB}\n{type(listB)}\t{len(listB)}")

print(listB[0]) # Accessing the first element of the list

#Middle element index = len(listB) // 2

middleIndex = len(listB) // 2
print(listB[middleIndex])

print(listB[-1]) # Accessing the last element of the list


mixed_list = ["Bijay", 20, 5.6, False, {
    "country": "Nepal",
    "city": "Itahari"
}]
print(mixed_list)

it_companies = ["Google", "Facebook", "Microsoft", "Apple", "IBM"]
print(f"{it_companies}\t{len(it_companies)}")

print(it_companies[0]) # Accessing the first company
print(it_companies[-1])
print(it_companies[len(it_companies) // 2]) # Accessing the middle company

it_companies.append("Amazon") # Adding 'Amazon' to the end of the list
print(it_companies)

it_companies.insert(0, "Twitter") # Adding 'Twitter' to the beginning of the list
print(f"{it_companies}\t{len(it_companies)}")

it_companies.insert(3, "LinkedIn") # Adding 'LinkedIn' to the middle of the list
print(f"{it_companies}\t{len(it_companies)}")

print(it_companies[0].upper()) # Changing 'Twitter' to uppercase

#Join the it_companies list with a string '#; ' as a separator
joined_companies = '#; '.join(it_companies)
print(joined_companies)


#check if a certain company exists in the it_companies

print("Google" in it_companies) # True
print("Netflix" in it_companies) # False

it_companies.sort() # Sorting the list in alphabetical order
print(it_companies)

it_companies.reverse() # Reversing the order of the list
print(it_companies)

sliced_companies = it_companies[3:6] # Slicing out the middle IT companies
print(sliced_companies)

sliced_companies.append("Netflix") # Adding 'Netflix' to the sliced list
print(sliced_companies)

sliced_companies.remove("Netflix") # Removing 'Netflix' from the sliced list
print(sliced_companies)

sliced_companies.clear() # Clearing all items from the sliced list
print(sliced_companies)
print(it_companies) # The original list remains unchanged

it_companies.clear() # Clearing all items from the original list
print(it_companies)

#Destroying the list
del it_companies
# print(it_companies) # This will raise an error since the list has been deleted


#clear vs del
# clear() method removes all items from the list but keeps the list itself, while del statement deletes the entire list from memory. After using clear(), the list will still exist but will be empty, while after using del, the list will no longer exist and any attempt to access it will result in an error.