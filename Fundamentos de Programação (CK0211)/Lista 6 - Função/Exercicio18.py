'''Create a subroutine that generates and displays the first three prime numbers above 100'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_above_100():
    primes = []
    num = 101  # Starting from 101, the first prime above 100
    while len(primes) < 3:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Calling the subroutine
prime_numbers = generate_primes_above_100()

# Displaying the result
print("The first three prime numbers above 100 are:", prime_numbers)
