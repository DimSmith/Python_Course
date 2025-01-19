capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
}

# Print Lille
print(travel_log["France"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "num_times_visited": 12,
        "cities_visited": ["Berlin", "Stuttgart"],
    },
}
# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][1])
