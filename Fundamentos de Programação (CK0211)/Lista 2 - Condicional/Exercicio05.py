'''Create a program that receives two numbers and performs the operations listed below, according to the user's choice.
USER'S CHOICE    OPERATION
1                Average of the entered numbers
2                Difference of the greater from the smaller
3                Product of the entered numbers
4                Division of the first by the second'''

# My signature 
print("=+"*28, "\n", " " * 20, "ALB System", "\n", "=+"*28, "\n")

# Receive two numbers
n1, n2 = input("Enter two numbers: ").split(" ")
n1 = float(n1)
n2 = float(n2)

print("What operation do you want?\n1 - Average\n2 - Difference\n3 - Product\n4 - Division")
choice = int(input())

if choice == 1:
    print(f"The average is {(n1 + n2) / 2}")
elif choice == 2:
    if n1 > n2:
        print(f"The difference is {n1 - n2}")
    else:
        print(f"The difference is {n2 - n1}")
elif choice == 3:
    print(f"The product is {n1 * n2}")
elif choice == 4:
    print(f"The division is {n1 / n2}")
else:
    print("ERROR")
