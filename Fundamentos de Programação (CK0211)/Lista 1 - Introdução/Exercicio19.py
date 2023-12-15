'''It is known that, to properly illuminate the rooms of a house, for each square meter, 18 W of power should be used. Create a program that receives the two dimensions of a room (in meters), calculates and shows its area (in m2), and the lighting power that should be used.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

width = float(input("Enter the width value: "))
length = float(input("Enter the length value: "))

area = width * length

print(f"{area * 18} W will be required for this room")
