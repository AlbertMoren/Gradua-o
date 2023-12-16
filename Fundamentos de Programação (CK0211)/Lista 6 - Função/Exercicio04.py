'''Create a subroutine that receives the radius of a sphere as a parameter, calculates and displays its volume in the main program: v = 4/3 * R3.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

radius = float(input("Enter the radius of the sphere: "))
print(f"The volume of the sphere is {calculate_sphere_volume(radius):.2f}")
