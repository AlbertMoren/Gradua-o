# A program that calculates and displays the multiplication table of a number entered by the user.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the number for which the multiplication table will be generated
number = int(input("Enter the number for the multiplication table: "))

# Display the multiplication table
print(f"{number} * {0}  = {number * 0}", " " * 10, f"{number} * {6}  = {number * 6}")
print(f"{number} * {1}  = {number}", " " * 10, f"{number} * {7}  = {number * 7}")
print(f"{number} * {2} = {number * 2}", " " * 10, f"{number} * {8}  = {number * 8}")
print(f"{number} * {3} = {number * 3}", " " * 10, f"{number} * {9}  = {number * 9}")
print(f"{number} * {4} = {number * 4}", " " * 10, f"{number} * {10}  = {number * 10}")
