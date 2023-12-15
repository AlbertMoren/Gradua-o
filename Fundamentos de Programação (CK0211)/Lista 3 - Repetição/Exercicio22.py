# Receive the age and height of several people, calculate and show the average height
# of those over 50 years old. To end data entry, enter age less than or equal to zero.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize variables
total_height = 0
count_people_over_50 = 0

# Data entry process
while True:
    age = int(input("Enter age (enter 0 or less to finish): "))

    if age <= 0:
        break

    height = float(input("Enter height: "))

    if age > 50:
        total_height += height
        count_people_over_50 += 1

# Calculate and display the average height for people over 50
if count_people_over_50 > 0:
    average_height_over_50 = total_height / count_people_over_50
    print(f"\nThe average height of people over 50 is: {average_height_over_50:.2f} meters")
else:
    print("\nNo data available for people over 50.")
