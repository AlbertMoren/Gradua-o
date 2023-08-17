'''Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.
IDADE                           |PESO
                | Até 60 | Entre 60 e 90 (inclusive)|  Acima de 90
Menores que 20  |    9   |       8                  |      7
De 20 a 50      |    6   |       5                  |      4
Maiores que 50  |    3   |       2                  |      1'''


#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

if(age <20):
    if(weight <=60):
        risk = 9
    elif(weight >60 and weight<=90):
        risk = 8
    else:
        risk = 7
elif(age >= 20 and age <=50):
    if(weight <=60):
        risk = 6
    elif(weight >60 and weight<=90):
        risk = 5
    else:
        risk = 4
else:
    if(weight <=60):
        risk = 3
    elif(weight >60 and weight<=90):
        risk = 2
    else:
        risk = 1

print(f"Your risk group is {risk}")