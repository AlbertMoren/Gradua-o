'''Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

peso = float(input("Insira seu peso: "))
print(f"Se voçe engorda 15%, fica com {peso+(peso*0.15)}")
print(f"Se voçe emagrecer 20%, fica com {peso-(peso*0.20)}")