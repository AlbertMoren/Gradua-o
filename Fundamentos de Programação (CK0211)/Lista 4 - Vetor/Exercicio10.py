# Fill a vector with ten integers and a second vector with five integers, calculate and show two resulting vectors.
# The first resulting vector will be composed of the sum of each even number from the first vector added to all numbers in the second vector.
# The second resulting vector will be composed of the number of divisors that each odd number from the first vector has in the second vector.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

vector1 = [0]*10
vector2 = [0]*5
result_vector1 = []
result_vector2 = []
divisor_count = 0

print("Fill vector 1")
for i in range(len(vector1)):
    vector1[i] = int(input(f"Element {i+1}º: "))

print("\nFill vector 2")
for i in range(len(vector2)):
    vector2[i] = int(input(f"Element {i+1}º: "))

for i in range(len(vector1)):
    if vector1[i] % 2 == 0:
        result_vector1.append(vector1[i] + sum(vector2))
    else:
        divisor_count = 0
        for j in range(len(vector2)):
            if vector1[i] % vector2[j] == 0:
                divisor_count += 1
        result_vector2.append(divisor_count)

print(f"{result_vector1}\n{result_vector2}")
