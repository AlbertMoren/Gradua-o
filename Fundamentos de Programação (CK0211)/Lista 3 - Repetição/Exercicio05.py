'''Create a program that shows the multiplication tables for numbers from 1 to 10'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n") 

for i in range(11):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    for j in range(11):
        print(f"{i} x {j} = {i*j}")
