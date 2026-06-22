
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

print(f"Min age: {ages[0]}")
print(f"Max age: {ages[-1]}")

#Middle age
middle_age = ages[len(ages) // 2]
print(f"Middle age: {middle_age}")

average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")


range = ages[-1] - ages[0]
print(f"Range of ages: {range}")

value1 = abs(ages[0] - average_age)
value2 = abs(ages[-1] - average_age)
print(f"Absolute difference between min age and average age: {value1:.2f}")
print(f"Absolute difference between max age and average age: {value2:.2f}")