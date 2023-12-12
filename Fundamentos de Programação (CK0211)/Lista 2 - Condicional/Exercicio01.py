'''Create a program that receives four grades from a student, calculates and displays the arithmetic average of the grades, and the message of approved or failed, considering 7 as the passing grade.'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the four grades
n1, n2, n3, n4 = input("Enter the student's 4 grades: ").split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

# Calculate the average
average = (n1 + n2 + n3 + n4) / 4

# Check if the student is approved or failed
if average >= 7:
    print("Student approved")
else:
    print("Student failed")
