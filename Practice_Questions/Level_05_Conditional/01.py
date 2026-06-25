
age = int(input("Enter your age: "))

if age >=18:
    print("You are eligible to drive")

else:
    print("You are not eligible to drive")
    remaining_years = 18 - age
    print("You will be eligible to drive after", remaining_years, "years.")


my_age = 22

if my_age == age:
    print("We are of the same age.")

elif my_age > age:
    print("I am older than you.")

    if my_age - age == 1:
        print(f"I am {my_age - age} year older than you.")
    else:
        print(f"I am {my_age - age} years older than you.")

else:
    print("You are older than me.")
    if age - my_age == 1:
        print(f"You are {age - my_age} year older than me.")
    else:
        print(f"You are {age - my_age} years older than me.")


