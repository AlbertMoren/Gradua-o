# Program Description:
# Create a program that fills an array with seven integer numbers, calculates, and shows:
# ■ numbers multiples of 2;
# ■ numbers multiples of 3;
# ■ numbers multiples of both 2 and 3.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize arrays
general_array = []
multiple_of_2 = []
multiple_of_3 = []
multiple_of_2_and_3 = []

# Fill the array with user input
for i in range(7):
    number = int(input("Enter a number: "))
    general_array.append(number)

# Separate numbers into different categories
for i in range(len(general_array)):
    if general_array[i] % 2 == 0 and general_array[i] % 3 == 0:
        multiple_of_2_and_3.append(general_array[i])
    elif general_array[i] % 2 == 0:
        multiple_of_2.append(general_array[i])
    elif general_array[i] % 3 == 0:
        multiple_of_3.append(general_array[i])

# Display results
print(f"Numbers multiples of 2 are {multiple_of_2}")
print(f"Numbers multiples of 3 are {multiple_of_3}")
print(f"Numbers multiples of both 2 and 3 are {multiple_of_2_and_3}")
