'''Make a subroutine that takes a positive integer N as a parameter and returns the sum of the integers between the number 1 and N (inclusive).'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_sum(n):
    sum_result = 0
    for i in range(n + 1):
        sum_result += i
    return sum_result

user_input = int(input("Enter a number: "))
result_sum = calculate_sum(user_input)
print(f"The sum of integers between 1 and {user_input} (inclusive) is: {result_sum}")
