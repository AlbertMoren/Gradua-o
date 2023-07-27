'''Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono. Sabe-se que ND = N * (N − 3)/2, em que N é o número de lados do polígono.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def calcular_diagonais_poligono(n_lados):
    if n_lados < 3:
        return 0
    diagonais = n_lados * (n_lados - 3) / 2
    return diagonais

# Receber o número de lados do polígono
n_lados = int(input("Digite o número de lados do polígono convexo: "))

# Calcular o número de diagonais
num_diagonais = calcular_diagonais_poligono(n_lados)

# Exibir o resultado
print(f"O número de diagonais do polígono convexo é: {num_diagonais}")
