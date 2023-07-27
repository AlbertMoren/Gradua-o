'''Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180 graus.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def calcular_terceiro_angulo(angulo1, angulo2):
    angulo3 = 180 - angulo1 - angulo2
    return angulo3

# Receber as medidas dos dois ângulos
angulo1 = float(input("Digite a medida do primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite a medida do segundo ângulo do triângulo: "))

# Calcular a medida do terceiro ângulo
angulo3 = calcular_terceiro_angulo(angulo1, angulo2)

# Exibir o resultado
print(f"A medida do terceiro ângulo do triângulo é: {angulo3:.2f} graus.")
