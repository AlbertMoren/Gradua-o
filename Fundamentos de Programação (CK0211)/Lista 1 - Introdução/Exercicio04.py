# Program that receives two grades, calculates, and displays the weighted average of these grades, considering a weight of 2 for the first and 3 for the second.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input two grades
x = float(input("Enter a grade: "))
y = float(input("Enter another grade: "))

# Calculate and print the weighted average
weighted_average = ((x * 2) + (y * 3)) / 5
print(weighted_average)