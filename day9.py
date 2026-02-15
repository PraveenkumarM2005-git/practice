age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 21 and age <= 60:
    if income > 30000:
        print("You are eligible for a loan")
    else:
        print("You are not eligible for a loan")
else:
    print("You are not eligible for a loan")
