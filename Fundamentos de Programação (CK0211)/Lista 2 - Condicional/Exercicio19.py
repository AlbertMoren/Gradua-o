'''Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
■ para homens: (72.7 * h) – 58.
■ para mulheres: (62.1 * h) – 44.7.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

height = float(input("Enter your height: "))
sex = input("Enter you gender: [M/F] ")

if (sex == "M" or sex == "m"):
    weight = (72.7 * height) - 58
elif(sex == "F" or sex == "f"):
    weight = (62.1 * height) - 44.7

print(f"Your ideal weight is {weight:.2f}")