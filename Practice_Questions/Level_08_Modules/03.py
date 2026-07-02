# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffleList(inputList):
    import random

    shuffledList = inputList[:]
    random.shuffle(shuffledList)
    return shuffledList

# Example usage
inputList = [1, 2, 3, 4, 5]
shuffledList = shuffleList(inputList)
print(f"Original list: {inputList}")
print(f"Shuffled list: {shuffledList}")

# Another example usage
inputList2 = ['apple', 'banana', 'cherry', 'date']
shuffledList2 = shuffleList(inputList2)
print(f"Original list: {inputList2}")
print(f"Shuffled list: {shuffledList2}")



# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def uniqueRandomNumbers():
    import random

    uniqueNumbers = random.sample(range(10), 7)
    return uniqueNumbers

# Example usage
randomNumbers = uniqueRandomNumbers()
print(f"Unique random numbers: {randomNumbers}")
print(f"Length of unique random numbers: {len(randomNumbers)}")