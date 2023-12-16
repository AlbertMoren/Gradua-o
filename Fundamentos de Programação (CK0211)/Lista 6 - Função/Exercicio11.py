'''Create a subroutine that receives as a parameter a positive integer value N, indicating the quantity
of installments of a sum S, calculated by the formula:
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... + (n2 + 1)/(n + 3)'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_sum(n):
    result = 0
    numerator = 2
    denominator = 4

    for _ in range(n):
        result += numerator / denominator
        numerator = (denominator ** 2) + 1
        denominator += 1

    return result

# Input the value of N
n = int(input("Enter the value of N: "))

# Calculate and print the sum
result_sum = calculate_sum(n)
print(f"The sum S for {n} parcels is: {result_sum:.4f}")
