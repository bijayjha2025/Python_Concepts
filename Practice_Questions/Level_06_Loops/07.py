# Loop through the countries and extract all the countries containing the word land.

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Thailand", "Poland", "Ireland"]
for country in countries:
    if "land" in country:
        print(country)



# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
reversedFruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversedFruits.append(fruits[i])
print("Reversed list:", reversedFruits)

