'''Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor)/2'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

diagonal_M,diagonal_m = input("Informe a diagonal maior e menor").split(" ")

diagonal_M = float(diagonal_M)
diagonal_m = float(diagonal_m)
area = (diagonal_M * diagonal_m)/2

print(f"A area é = {area:.2f}")
