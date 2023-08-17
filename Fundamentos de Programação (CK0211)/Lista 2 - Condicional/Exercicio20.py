'''Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir. Para idade inferior a 5, deverá mostrar mensagem.
CATEGORIA   | IDADE
Infantil    |5 a 7
Juvenil     |8 a 10
Adolescente |11 a 15
Adulto      |16 a 30
Sênior      |Acima de 30'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))

if(age >= 5 and age <= 7):
    print("Your category is children")
elif(age >= 8 and age <= 10):
    print("Your category is young")
elif(age >= 11 and age <= 15):
    print("Your category is adolescent")
elif(age >= 16 and age <= 30):
    print("Your category is adult")
elif(age > 30):
    print("Your category is senior")
else:
    print("you don't fit into any category")