print("Welcome toh the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    age = int(input("Enter your age: "))
    print("Yoc can enjoy the ride")
    if age <= 12:
        bill = 5
        print("The cost for ride will be $5")
    # elif
    elif age <= 18:
        bill = 7
        print("The cost for ride will be $7")
    elif 45 <= age <= 55:
        print("Everything is going to be alright ,take free ride")
    else:
        bill = 12
        print("The cost for ride will be $12")

    wants_photo = input("Do you want to have a Photo ? y for Yes and n for No")
    if wants_photo == "y":
        bill += 3
    print(f"Your Final bill is ${bill}")
else:
    print("Sorry you cant ride")
