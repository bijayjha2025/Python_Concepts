# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.

month = input("Enter the month: ")

#Creating four lists for each season with the corresponding months
autumnMonths = ['September', 'October', 'November']
winterMonths = ['December', 'January', 'February']
springMonths = ['March', 'April', 'May']
summerMonths = ['June', 'July', 'August']

if month in autumnMonths:
    print(f"It is autumn season and the month is {month}")

elif month in winterMonths:
    print(f"It is winter season and the month is {month}")

elif month in springMonths:
    print(f"It is spring season and the month is {month}")

elif month in summerMonths:
    print(f"It is summer season and the month is {month}")

else:
    print("Invalid month. Please enter a valid month name.")