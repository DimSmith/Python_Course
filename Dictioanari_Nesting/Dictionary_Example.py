# Dictionary Name = { Key:Value }
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
}

print(colours["pear"])
print(colours)

# Add new
colours["grape"] = "purple"
print(colours)
print("------")

# Clear the dictionary
# colours = {}
# print(colours)
# print("------")


# Edit the dictionary
colours["pear"] = "orange"
print(colours)
print("------")

# Loop through dictionary
for key in colours:
    print(key)
    print(colours[key])
    print("------")
