def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_two_numbers(15, 5)
print("The sum of 15 and 5 is:", result)


def area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

circleArea = area_of_circle(5)
print(f"The area of the circle with radius 5 is: {circleArea:.2f}")



# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)): #isinstance() function is used to check if the argument is an instance of a specified class or a subclass thereof. In this case, it checks if num is an instance of either int or float.
            total += num
        else:
            print(f"Warning: '{num}' is not a number and will be ignored.")
    return total

result = add_all_nums(10, 20, 30, 'a', 40.5, 'b', 50)
print("The sum of all valid numbers is:", result)


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatureconverted = convert_celsius_to_fahrenheit(25)
print(f"25°C is equivalent to {temperatureconverted}°F")