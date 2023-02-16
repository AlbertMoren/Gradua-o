'''Faça um programa que receba dez números, calcule e mostre a soma dos números pares e a soma dos números primos.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

pares = 0
cont = 0
pimos = 0
for i in range(10):
    numero = int(input("Número? "))
    if(numero%2==0):
        pares+=numero
    for j in range(numero):
        cont = 0
        if(numero == 1):
            cont = 2
        elif(numero%j==0):
            cont+=1
    if(cont>2):
       pimos += numero
print(f"A soma dos pars é {pares} a soma dos primos é {pimos}")