print("Welcome to the best Tip Calculator")
bill_price = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to plit the bill ?"))
bill_with_tip= bill_price + tip/100*bill_price
each_price = bill_with_tip/people
final=round(each_price,2)
print(f"Each person should pay {final}")
