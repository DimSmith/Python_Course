fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])

fruits[1] = "Orange"
print(fruits)

# add one item to end of the list
fruits.append("Apple")
print(fruits)

# add list of items to end of the list
fruits.extend(["Melon","Watermelon"])
print(fruits)