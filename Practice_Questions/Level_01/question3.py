#To find area and circumference of a circle

PI = 3.14 #This is a constant
radius = float(input("Enter the radius of the circle:"))
area = PI * radius * radius
circumference = 2 * PI * radius


print(f"Area of circle is: {area:.2f}")
print(f"Circumference of circle is: {circumference:.2f}")


