'''Create a program that receives a number, calculates, and shows the multiplication table for that number'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

number = int(input("Which multiplication table? "))
for i in range(11):
    print(f"{number} x {i} = {number*i}")
