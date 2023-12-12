'''Create a program that receives two numbers and displays the smallest one'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the two numbers
n1, n2 = input("Enter 2 numbers: ").split(" ")
n1 = int(n1)
n2 = int(n2)

# Compare the numbers and display the smallest one
if n1 >= n2:
    print(f"The number {n2} is the smallest.")
else:
    print(f"The number {n1} is the smallest.")
