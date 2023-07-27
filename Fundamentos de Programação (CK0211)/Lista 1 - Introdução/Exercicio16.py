'''Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa'''

import math

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")


cateto1 = float(input("Valor do cateto 1: "))
cateto2 = float(input("Valor do cateto 2: "))

hipo = math.sqrt(pow(cateto1,2) + pow(cateto2,2))

print(f"A hipotenusa = {hipo:.2f}")