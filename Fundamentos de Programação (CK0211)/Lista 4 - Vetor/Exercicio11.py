# Receive ten integers and store them in a vector. Calculate and show two resulting vectors:
# the first one with even numbers, and the second one with odd numbers.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

numbers = [0] * 10
even_numbers = []
odd_numbers = []

print("Enter ten integers:")
for i in range(10):
    numbers[i] = int(input(f"Number {i+1}: "))

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
