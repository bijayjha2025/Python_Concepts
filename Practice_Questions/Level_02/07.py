# Convert days into years, months, days

days = int(input("Enter total days: "))
years = days // 365
months = (days % 365) // 30
days = days % 30
print(f"Years: {years}, Months: {months}, Days: {days}")