'''Create a program that receives ten numbers, calculates and shows the sum of the even numbers and the sum of the prime numbers.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

sum_even = 0
sum_primes = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(10):
    number = int(input("Number? "))
    if number % 2 == 0:
        sum_even += number
    if is_prime(number):
        sum_primes += number

print(f"The sum of even numbers is {sum_even} and the sum of prime numbers is {sum_primes}")
