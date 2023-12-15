# minha assinatura
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

vetor = [0] * 10
cont_negativos = 0
soma_positivos = 0

# Input for each element in the vector
for i in range(len(vetor)):
    vetor[i] = float(input("Insert a real number (positive or negative): "))
    if vetor[i] < 0:
        cont_negativos += 1
    else:
        soma_positivos += vetor[i]

# Displaying the results
print(f"Number of negative numbers: {cont_negativos}")
print(f"Sum of positive numbers: {soma_positivos}")
