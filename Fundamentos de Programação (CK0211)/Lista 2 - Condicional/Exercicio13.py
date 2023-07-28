'''Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

value = float(input("Enter product value: R$"))

if( value <= 50.00):
    value = value *1.05
elif(value>50.00 and value<100.00):
    value = value*1.10
else:
    value = value*1.15


if(value <= 80):
    classification = "cheap"
elif(value >80.00 and value<=120.00):
    classification = "Normal"
elif(value > 120.00 and value<=200.00):
    classification = "Dear"
else:
    classification = "Very expensive"

print(f"The producit will cust {value} and the rating is {classification}")