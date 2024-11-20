print("Welcome toh the rollercoaster!")
height = int(input("What is your height in cm?"))


if height >= 120:
    age = int(input("Enter your age: "))
    print("Yoc can enjoy the ride")
    if age <= 12:
        print("The cost for ride will be $5")
    # elif
    elif age <= 18:
        print("The cost for ride will be $7")
    else:
        print("The cost for ride will be $12")
else:
    print("Sorry you cant ride")


