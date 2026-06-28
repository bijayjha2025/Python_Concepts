# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

total = 0
for i in range(0, 101):
    total += i
print(total)


# Use for loop to iterate from 0 to 100 and print the sum of all even numbers and sum of all odd numbers.

totalEven = 0
totalOdd = 0

for i in range(0, 101):
    if i % 2 == 0:
        totalEven += i
    else:
        totalOdd += i
print("Sum of even numbers:", totalEven)
print("Sum of odd numbers:", totalOdd)