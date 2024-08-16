# Take a list of names as input from the user
names = input("Enter the names separated by commas: ").split(',')

# Strip any extra whitespace from the names
names = [name.strip() for name in names]

# Find the bronze medalist (the third person in the list)
if len(names) >= 3:
    bronze_medalist = names[2]
    print(f"The bronze medal goes to: {bronze_medalist}")
else:
    print("Not enough participants to determine a bronze medalist.")