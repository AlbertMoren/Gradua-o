# A program that receives a person's weight in kilograms, calculates and displays that weight in grams.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the weight in kilograms
weight_kg = float(input("Enter the weight in kg: "))

# Calculate and print the weight in grams
print(f"The weight in grams is {weight_kg * 1000:.2f}g")
