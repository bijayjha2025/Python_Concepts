#To convert Celsius to Fahrenheit and Fahrenheit to Celsius

celsius = float(input("Enter temperature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degree celsius is equal to {fahrenheit:.2f} degree fahrenheit")


fahrenheit = float(input("Enter temperature in Fahrenheit:"))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} degree fahrenheit is equal to {celsius:.2f} degree celsius")
