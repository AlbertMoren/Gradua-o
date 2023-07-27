'''Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e a distância em que a escada está da parede, calcule e mostre a medida da escada para que se possa alcançar
sua ponta.'''

import math

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")


def calcular_comprimento_escada(angulo_graus, distancia_parede):
    # Converter o ângulo de graus para radianos
    angulo_radianos = math.radians(angulo_graus)

    # Calcular o comprimento da escada usando o seno do ângulo
    comprimento_escada = distancia_parede / math.sin(angulo_radianos)

    return comprimento_escada

# Receber as entradas do usuário
angulo = float(input("Digite o ângulo da escada (em graus): "))
distancia = float(input("Digite a distância da escada à parede: "))

# Calcular o comprimento da escada
comprimento = calcular_comprimento_escada(angulo, distancia)

# Exibir o resultado
print(f"A medida da escada necessária é: {comprimento:.2f} unidades.")
