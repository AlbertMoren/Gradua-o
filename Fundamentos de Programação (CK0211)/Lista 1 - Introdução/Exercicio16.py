# Receive the values of the legs of a triangle, calculate and show the value of the hypotenuse

import math

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

leg1 = float(input("Value of leg 1: "))
leg2 = float(input("Value of leg 2: "))

hypotenuse = math.sqrt(pow(leg1, 2) + pow(leg2, 2))

print(f"The hypotenuse = {hypotenuse:.2f}")
