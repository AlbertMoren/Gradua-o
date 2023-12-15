'''Create a program that receives three numbers and displays the smallest one'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the three numbers
n1, n2, n3 = input("Enter 3 numbers: ").split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

# Find the smallest number
smallest = n1
if n2 < smallest or n3 < smallest:
    if n2 < n3:
        smallest = n2
        print(f"The {n2} is the smallest of all.")
    else:
        smallest = n3
        print(f"The {n3} is the smallest of all.")
else:
    print(f"The {smallest} is the smallest of all.")
