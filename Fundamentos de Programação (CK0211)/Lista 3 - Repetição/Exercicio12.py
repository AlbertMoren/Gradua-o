'''Create a program that receives ten integers and shows the quantity of prime numbers among the entered numbers.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

for i in range(10):
    number = int(input("Enter a number: "))
    numberF = float(number)
    div = 0
    for j in range(number):
        if numberF % (j+1) == 0:
            div += 1
    if div == 2:
        print(number)
