# Ask the user to input 5 strings separated by spaces
user_input = input("Enter 5 strings separated by spaces: ")

# Split the input string into a list of strings
my_list = user_input.split()

# Check if the list has exactly 5 items
if len(my_list) != 5:
    print("Please enter exactly 5 strings.")
else:
    # Extract the first and last items from the list
    first_item = my_list[0]
    last_item = my_list[-1]

    # Create the output sentence
    output = f"Some animals {first_item} and some {last_item}"

    # Print the result
    print(output)