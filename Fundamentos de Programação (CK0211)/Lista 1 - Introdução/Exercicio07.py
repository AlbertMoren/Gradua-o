# A program that receives a person's weight, calculates and displays:
# a) the new weight if the person gains 15% of the entered weight;
# b) the new weight if the person loses 20% of the entered weight.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the person's weight
weight = float(input("Enter your weight: "))

# Calculate and print the new weight if the person gains 15%
print(f"If you gain 15%, your weight will be {weight + (weight * 0.15)}")

# Calculate and print the new weight if the person loses 20%
print(f"If you lose 20%, your weight will be {weight - (weight * 0.20)}")
