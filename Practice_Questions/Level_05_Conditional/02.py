number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))


if number1 > number2:
    print(f"{number1} is greater than {number2}.")

elif number2 > number1:
    print(f"{number2} is greater than {number1}.")

else:
    print(f"{number1} is equal to {number2}.")


