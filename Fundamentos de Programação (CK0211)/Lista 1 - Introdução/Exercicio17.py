'''Create a program that receives the radius, calculates, and shows:
a) the circumference of a sphere; where C = 2 * pi R;
b) the area of a sphere; where A = pi R2;
c) the volume of a sphere; where V = ¾ * pi R3'''

import math

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

radius = float(input("Enter the radius: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
volume = (3/4) * math.pi * pow(radius, 3)

print(f" Circumference = {circumference:.2f}, Area = {area:.2f}, and Volume = {volume:.2f}")
