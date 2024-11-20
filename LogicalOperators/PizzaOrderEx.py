print("Welcome to Mario Pizza Delivery!")
size = input("What size pizza do you want? S,M or L: ")
meat = input("Do you want pepperoni on your Pizza? Y or N:  ")
extra = input("Do you want extra cheese on your Pizza? Y or N: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("We dont have this size")

if extra == "Y":
    bill += 1

if meat == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
print(f"Your Final Price is : ${bill}")
