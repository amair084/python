# Aaron Mairel
# CIS150AB 28881
# Oct 29, 2025
# Lists and Dictionaries Assignment
# Task1: Create a list of lists containing names and ages
# Task2: Concatenate dictionaries into a single dictionary using unique keys
# Task3: Remove a city from the merged dictionary

# Task 1: - Create a list of lists containing names and ages

# First, get the names and ages into lists
names = ["London", "James", "Ahmad"]
ages = [16, 20, 24]

# Combine the List
combined_list = [names, ages]

# Now, print the outputs
print(f"Combined List: {combined_list}")
print(f"Names: {combined_list[0]}")
print(f"Ages: {combined_list[1]}")

# Task 2: - Concatenate dictionaries into a single dictionary using unique keys
print()

# First, we need to get the original city dictionaries
australianCities = {1: "Sydney", 2: "Brisbane"}
newZealandCities = {1: "Auckland", 2: "Wellington", 3: "Christchurch"}
arizonaCities = {1: "Mesa", 2: "Phoenix", 3: "Flagstaff"}

# Create the merge dictionary
merged_cities = {}

# Now, create the unique keys based on where the cities are located. I chose this method because it seemed quite easy to understand
# and used the same keys as before, so nothing really changed except that we know which state/country the city belongs to

for key, city in australianCities.items():
    merged_cities[f"AUS{key}"] = city

for key, city in newZealandCities.items():
    merged_cities[f"ZEA{key}"] = city

for key, city in arizonaCities.items():
    merged_cities[f"ARZ{key}"] = city

# Then, print the merged city list

print(f"Merged City List: {merged_cities}")

# Task 3: - Remove a city from the merged dictionary
print()

# Remove Flagstaff (ARZ3 in the merged dictionary)
merged_cities.pop("ARZ3")

#Finally, print the merged city list without flagstaff
print(f"Final City List: {merged_cities}")

