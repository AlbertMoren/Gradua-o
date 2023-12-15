'''Create a program that receives two numbers and performs one of the operations listed below, according to the user's choice. If an invalid option is entered, show an error message and terminate the program. The options are:
a) The first number raised to the power of the second number.
b) Square root of each of the numbers.
c) Cube root of each of the numbers.'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive two numbers
n1, n2 = input("Enter two numbers: ").split(" ")
n1 = float(n1)
n2 = float(n2)

print("What operation do you want?\n1 - The first raised to the power of the second\n2 - Square root of each\n3 - Cube root of each")
choice = int(input())

if choice == 1:
    print(f"The first raised to the power of the second is {n1 ** n2}")
elif choice == 2:
    print(f"The square root of {n1} is {n1 ** 0.5:.2f} and of {n2} is {n2 ** 0.5:.2f}")
elif choice == 3:
    print(f"The cube root of {n1} is {n1 ** (1/3):.2f} and of {n2} is {n2 ** (1/3):.2f}")
else:
    print("ERROR")
