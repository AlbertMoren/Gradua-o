'''Create a program that receives several ages, calculates, and shows the average of the entered ages. Finish by entering age equal to zero.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

print("Enter 0 to exit")
counterAge = 0
ages = 0

while True:
    age = int(input("Enter your age: "))
    counterAge += 1
    ages += age
    if age == 0:
        break

print(f"The average age entered is {ages/counterAge:.2f}")
