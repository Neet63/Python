age = int(input("Enter your Age : "))

if age>=18 and age<=70:
    print("You can drive")
else:
    if age<18:
        print("You are under age to drive")
    else:
        print("Your age is too much to drive ")