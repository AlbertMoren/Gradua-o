'''Faça um programa que receba um número, calcule e mostre a tabuada desse número'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

number = int(input("Qual tabuada? "))
for i in range(11):
    print(f"{number} x {i} = {number*i}")
