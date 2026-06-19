#Calculate percentage from marks obtained in 5 subjects.

#Without using list or loop
marks1 = float(input("Enter marks obtained in subject 1: "))
marks2 = float(input("Enter marks obtained in subject 2: "))
marks3 = float(input("Enter marks obtained in subject 3: "))
marks4 = float(input("Enter marks obtained in subject 4: "))
marks5 = float(input("Enter marks obtained in subject 5: "))

totalMarks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (totalMarks / 500) * 100
print(f"Total Marks: {totalMarks} out of 500")
print(f"Percentage: {percentage:.2f}%")