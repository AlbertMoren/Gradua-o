'''Faça um programa que receba:
■ o código do produto comprado; e
■ a quantidade comprada do produto.
Calcule e mostre:
■ o preço unitário do produto comprado, seguindo a Tabela I;
■ o preço total da nota;
■ o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e
■ o preço final da nota depois do desconto'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

code_product = int(input("Enter the product code: "))
amount = int(input("How many: "))

if code_product > 0 and code_product <= 10:
    price = 10.00
elif code_product > 10 and code_product <= 20:
    price = 15.00
elif code_product > 20 and code_product <= 30:
    price = 15.00
elif code_product > 30 and code_product <= 40:
    price = 15.00

total = price * amount

if total <= 250:
    total = total * 0.95
elif total > 250 and total <= 500:
    total = total * 0.90
else:
    total = total * 0.85

print(f"total note price is {total:.2f}")