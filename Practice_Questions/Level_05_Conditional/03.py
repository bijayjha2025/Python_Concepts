
marks = int(input("Enter your percentage marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")

else:
    if marks >= 90:
        print("You have scored an A+ grade.")

    elif marks >= 80 and marks < 90:
        print("You have scored an A grade.")

    elif marks >= 70 and marks < 80:
        print("You have scored a B grade.")
        
    elif marks >= 60 and marks < 70:
        print("You have scored a C grade.")

    else:
        print("You have scored a D grade.")