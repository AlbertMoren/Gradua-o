'''Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio no último ano. Faça um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito. SALDO MÉDIO PERCENTUAL
Acima de R$ 400,00 30% do saldo médio
R$ 400,00 R$ 300,00 25% do saldo médio
R$ 300,00 R$ 200,00 20% do saldo médio
Até R$ 200,00 10% do saldo médio'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

media = float(input("Valor médio do cliente: R$"))
if(media > 400):
    print(f"Seu crédito séra de {(media + (media*0.3)):.2f}")
elif(media <= 400 and media >300):
    print(f"Seu crédito séra de {(media + (media*0.25)):.2f}")
elif(media <= 300 and media >200):
    print(f"Seu crédito séra de {(media + (media*0.2)):.2f}")
elif(media <= 200):
    print(f"Seu crédito séra de {(media + (media*0.1)):.2f}")