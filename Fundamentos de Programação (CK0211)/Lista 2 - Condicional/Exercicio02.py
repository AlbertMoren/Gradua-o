'''Create a program that receives two grades, calculates and displays the arithmetic average, and the message found in the following table:'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the two grades
n1, n2 = input("Enter the student's 2 grades: ").split(" ")
n1 = float(n1)
n2 = float(n2)

# Calculate the average
average = (n1 + n2) / 2

# Check the range and display the corresponding message
if 0 <= average < 3:
    print("Failed")
elif 3 <= average < 7:
    print("Exam")
else:
    print("Approved")
