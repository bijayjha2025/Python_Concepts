
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)  # False

print("Iceland" in nordic_countries)  # True



# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("apple", "banana", "papaya", "mango")
vegetables = ("carrot", "broccoli", "spinach", "cabbage")
animal_products = ("milk", "cheese", "yogurt", "butter")

food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:", food_stuff_lt)

#Slice out the middle item
middle_item = food_stuff_lt[len(food_stuff_lt)//2]
print("Middle item:", middle_item)


# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)  # This will raise an error since food_stuff_tp has been deleted