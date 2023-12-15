# Program Description:
# Create a program that fills a vector with fifteen integer elements and checks for the existence of elements equal to 30, showing the positions where they appeared.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize list and positions
lista = []
posicoes = []

# Fill the list with fifteen elements
for i in range(15):
    valor = int(input("Enter a value: "))
    lista.append(valor)

# Check for positions with element equal to 30
for i in range(len(lista)):
    if lista[i] == 30:
        posicoes.append(i + 1)

# Display results
if not posicoes:
    print("No value equal to 30 in the list.")
else:
    print("Values equal to 30 are in positions:", end="")
    for pos in posicoes:
        print(f" {pos}", end="")
