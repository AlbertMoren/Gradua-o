'''Faça um programa que receba o raio, calcule e mostre:
a) o comprimento de uma esfera; sabe-se que C = 2 * pi R;
b) a área de uma esfera; sabe-se que A = pi R2;
c) o volume de uma esfera; sabe-se que V = ¾ * pi R3'''

import math

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

raio = float(input("Informe o raio: "))

a = 2 * math.pi * raio
b = math.pi * pow(raio,2)
c = (3/4) * math.pi * pow(raio,3)

print(f" comprimento = {a:.2f}, a área = {b:.2f} e o volume = {c:.2f}")