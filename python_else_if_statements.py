# age = 14

# if age > 10:
#     print("You can go to the movies.")
# else:
#     print("You cannot go to the movies.")
#     age = 18

# if age < 13:
#     print("You're a child.")
# elif age < 18:
#     print("You're a teenager.")
# elif age < 65:
#     print("You're an adult.")
# else:
#     print("You're a senior.")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print("The first number is larger.")
# elif num1 < num2:
#     print("The second number is larger.")
# else:
#     print("The numbers are the same.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

equal_count = 0

if num1 == num2 == num3:
    equal_count = 3
elif num1 == num2 or num1 == num3 or num2 == num3:
    equal_count = 2
else:
    equal_count = 0

print(equal_count)