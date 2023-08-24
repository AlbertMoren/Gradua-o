'''Faça um programa que receba a idade e a altura de várias pessoas, calcule e mostre a média das alturas daquelas com mais de 50 anos. Para encerrar a entrada de dados, digite idade menor ou igual a zero.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

totalAge = 0
contAge = 0

while True:
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    if age <= 0:
        break
    if age >= 50:
        totalAge+= age
        contAge+= 1

print(f"The everage age of people over 50 is {totalAge/contAge:.2f}")