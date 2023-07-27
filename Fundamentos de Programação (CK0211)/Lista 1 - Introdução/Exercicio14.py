'''Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

anoNasc = int(input("Qual seu ano de nascimento? "))
anoAtual = int(input("Qual o ano atual? "))

anos = anoAtual - anoNasc
mes = anos*12
dias = anos*365
semanas = anos*52

print(f"Voce tem {anos} de idade em anos")
print(f"Voce tem {mes} de idade em meses")
print(f"Voce tem {dias} de idade em dias")
print(f"Voce tem {semanas} de idade em semanas")