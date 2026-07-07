from datetime import datetime

now = datetime.now() #This gives the current date and time
print("Current date and time: ", now)

print("Current year: ", now.year) #This gives the current year
print("Current month: ", now.month) #This gives the current month
print("Current day: ", now.day) #This gives the current day of the month
print("Current hour: ", now.hour) #This gives the current hour
print("Current minute: ", now.minute) #This gives the current minute
print("Current second: ", now.second) #This gives the current second

print("Current date and time in ISO format: ", now.isoformat()) #This gives the current date and time in ISO format
print("Current date and time in string format: ", now.strftime("%Y-%m-%d %H:%M:%S")) #This gives the current date and time in string format
print(datetime.timestamp(now)) #This gives the current date and time in timestamp format


#Using date from datetime module
from datetime import date

today = date.today() #This gives the current date
print("Current date: ", today)


#Time object: The time object represents a time of day, independent of any particular day. It has attributes for hour, minute, second, microsecond, and tzinfo (time zone information).
from datetime import time

a = time(12, 30, 45) #This creates a time object with hour=12, minute=30, second=45
print("Time object: ", a)
print("Hour: ", a.hour) #This gives the hour of the time object
print("Minute: ", a.minute) #This gives the minute of the time object
print("Second: ", a.second) #This gives the second of the time object


#difference between two points in time: We can calculate the difference between two points in time using the timedelta object from the datetime module. The timedelta object represents a duration, i.e., the difference between two dates or times.

from datetime import timedelta

t1 = datetime(2023, 1, 1, 12, 0, 0) #This creates a datetime object for January 1, 2023 at 12:00:00
t2 = datetime(2023, 1, 2, 12, 0, 0) #This creates a datetime object for January 2, 2023 at 12:00:00
print("Difference between two points in time: ", t2 - t1) #This gives the difference between two points in time


# Questions.

# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)
print(datetime.timestamp(now))



# Format the current date using this format: "%m/%d/%Y, %H:%M:%S"

from datetime import datetime
now = datetime.now()
formattedDate = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date: ", formattedDate)


# Today is 7 July 2026. Change this string into date
from datetime import datetime
dateString = "7 July, 2026"
dateObject = datetime.strptime(dateString, "%d %B, %Y")
print("Date object: ", dateObject)
