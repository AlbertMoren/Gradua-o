'''Uma empresa decide aplicar descontos nos seus preços usando a tabela a seguir. Faça um programa que receba o preço atual de um produto e seu código, calcule e mostre o valor do desconto e o novo preço.
PREÇO ATUAL                |% DE DESCONTO
Até R$ 30,00               |Sem desconto
Entre R$ 30,00 e R$ 100,00 |10%
Acima de R$ 100,00         |15%'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

value,code = input("Enter the value of the product and its code: ").split(" ")

value = float(value)

discout = value * 0
if(value >30 and value <100):
    newValue = value * 0.9
    discout = value - newValue
elif(value >= 100):
    newValue = value * 0.85
    discout = value - newValue

print(f"The product {code} will have R${discout:.2f} discount and have a new price of R${newValue:.2f}")