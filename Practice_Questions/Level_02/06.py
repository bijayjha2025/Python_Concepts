#WAP to convert total seconds into hours, minutes and seconds.

seconds = int(input("Enter total seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")