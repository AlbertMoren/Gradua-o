# João received his salary and needs to pay two overdue bills. Due to the delay, he must pay
# a 2% fine on each bill. Create a program that calculates and shows how much of João's salary
# will remain.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input João's salary and the values of the overdue bills
salary = float(input("What is your salary? "))
bill1 = float(input("What is the value of your first bill? "))
bill2 = float(input("What is the value of your second bill? "))

# Apply a 2% fine to each bill
bill1 *= 1.02
bill2 *= 1.02

# Calculate the remaining salary after paying the bills
salary -= bill1 + bill2

print(f"João will have R${salary:.2f} remaining from his salary.")
