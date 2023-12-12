'''Create a program that receives the angle formed by a ladder leaning on the ground and the distance the ladder is from the wall, calculates and shows the length of the ladder needed to reach its tip.'''

import math

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def calculate_ladder_length(angle_degrees, wall_distance):
    # Convert the angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the length of the ladder using the sine of the angle
    ladder_length = wall_distance / math.sin(angle_radians)

    return ladder_length

# Receive user inputs
angle = float(input("Enter the angle of the ladder (in degrees): "))
distance = float(input("Enter the distance from the ladder to the wall: "))

# Calculate the length of the ladder
length = calculate_ladder_length(angle, distance)

# Display the result
print(f"The required length of the ladder is: {length:.2f} units.")
