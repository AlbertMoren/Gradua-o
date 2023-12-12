'''Create a program that receives the measure of two angles of a triangle, calculates, and shows the measure of the third angle. It is known that the sum of the angles of a triangle is 180 degrees.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def calculate_third_angle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    return angle3

# Receive the measures of the two angles
angle1 = float(input("Enter the measure of the first angle of the triangle: "))
angle2 = float(input("Enter the measure of the second angle of the triangle: "))

# Calculate the measure of the third angle
angle3 = calculate_third_angle(angle1, angle2)

# Display the result
print(f"The measure of the third angle of the triangle is: {angle3:.2f} degrees.")
