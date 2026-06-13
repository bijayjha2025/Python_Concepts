
#To swap two numbers

number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))


#Using a temporary variable
temp = number1
number1 = number2
number2 = temp

print(f"After swapping, first number is: {number1}")
print(f"After swapping, second number is: {number2}")



#Without using a temporary variable
number1, number2 = number2, number1
print(f"After swapping, first number is: {number1}")
print(f"After swapping, second number is: {number2}")