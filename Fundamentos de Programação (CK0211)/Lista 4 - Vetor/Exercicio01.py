# Program Description:
# Create a program that fills an array with six integer elements. Calculate and show:
# ■ all even numbers;
# ■ the quantity of even numbers;
# ■ all odd numbers;
# ■ the quantity of odd numbers.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize arrays and counters
general_array = []
even_array = []
even_count = 0
odd_array = []
odd_count = 0

# Fill the array with user input
for i in range(6):
    number = int(input("Enter a number: "))
    general_array.append(number)

# Separate even and odd numbers
for i in range(len(general_array)):
    if general_array[i] % 2 == 0:
        even_array.append(general_array[i])
        even_count += 1
    else:
        odd_array.append(general_array[i])
        odd_count += 1

# Display results
print(f"We have a total of {even_count} even numbers, which are {even_array}")
print(f"We have a total of {odd_count} odd numbers, which are {odd_array}")
