# Receive five numbers and show the output as described:
# "Digite o 1º número", "Digite o 2º número", ..., "Digite o 5º número".
# Display the sum of the entered numbers.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

numbers = []
for i in range(5):
    number = int(input(f"Enter the {i+1}st number: "))
    numbers.append(number)

sum_of_numbers = sum(numbers)
formatted_numbers = " + ".join(map(str, numbers))
print(f"The entered numbers are: {formatted_numbers} = {sum_of_numbers}.")
