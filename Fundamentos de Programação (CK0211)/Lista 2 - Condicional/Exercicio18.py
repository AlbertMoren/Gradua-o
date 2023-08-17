'''Faça um programa que receba a idade de uma pessoa e mostre a mensagem de maioridade ou não.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are of legal age")
else:
    print("you are not of legal age")