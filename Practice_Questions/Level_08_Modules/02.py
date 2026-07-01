# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def listOfHexaColors(numColors):
    import random

    hexChars = '0123456789abcdef'
    hexaColors = ['#' + ''.join(random.choice(hexChars) for _ in range(6)) for _ in range(numColors)]
    return hexaColors

numColors = int(input("Enter the number of hexadecimal colors to generate: "))
hexaColors = listOfHexaColors(numColors)
print(f"Generated hexadecimal colors: {hexaColors}")


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def listOfRgbColors(numColors):
    import random

    rgbColors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(numColors)]
    return rgbColors

numColors = int(input("Enter the number of RGB colors to generate: "))
rgbColors = listOfRgbColors(numColors)
print(f"Generated RGB colors: {rgbColors}")


# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generateColors(colorType, numColors):
    if colorType == 'hexa':
        return listOfHexaColors(numColors)
    elif colorType == 'rgb':
        return listOfRgbColors(numColors)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
    
colorType = input("Enter the color type (hexa/rgb): ")
numColors = int(input("Enter the number of colors to generate: "))  

print(f"Generated colors: {generateColors(colorType, numColors)}")
