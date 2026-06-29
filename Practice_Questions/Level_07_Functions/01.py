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



# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def checkSeason(month):
    month = month.lower()  # Convert the input to lowercase for case-insensitive comparison

    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    
    elif month in ['march', 'april', 'may']:
        return "Spring"
    
    elif month in ['june', 'july', 'august']:
        return "Summer"
    
    else:
        return "Invalid month. Please enter a valid month name."
    
result = checkSeason("March")
print(f"March is in the {result} season.")

# Write a function called calculate_slope which return the slope of a linear equation

def calculateSlope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    slope = (y2 - y1) / (x2 - x1)
    return slope

slopeResult = calculateSlope(2, 3, 6, 6)
print(f"The slope of the line passing through points (2, 3) and (6, 6) is: {slopeResult}")



#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solveQuadraticEquation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    
    elif discriminant == 0:
        root = -b / (2*a)
        return root,

    else:
        return "No real roots."
    


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def printList(inputList):
    for element in inputList:
        print(element)

resultList = [1, 2, 3, 4, 5]
printList(resultList)