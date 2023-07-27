'''Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$ 1,80; do marco alemão, de R$ 2,00; e da libra esterlina, de R$ 3,57. O programa deve fazer as conversões e mostrá-las'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

real = float(input("Insira o valor: R$"))

print(f" Em dolar é {(real/1,80):.2f}")
print(f" Em Marco alemão é {(real/2):.2f}")
print(f" Em Libra esterlina é {(real/3.57):.2f}")