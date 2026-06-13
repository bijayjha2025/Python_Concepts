#WAP to find simple interest

principal = float(input("Enter principal amount:"))
rate = float(input("Enter rate of interest:"))
time = float(input("Enter time period(in years):"))


simpleInterest = (principal * rate * time) / 100
print(f"Simple Interest is: {simpleInterest:.2f}")

totalAmount = principal + simpleInterest
print(f"Total Amount after {time} years is: {totalAmount:.2f}")

