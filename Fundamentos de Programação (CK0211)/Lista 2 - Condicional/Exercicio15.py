'''Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir. Faça um programa que receba o tipo de investimento e seu valor, calcule e mostre o valor corrigido após um mês de investimento, de acordo com o tipo de investimento.
TIPO |DESCRIÇÃO            |RENDIMENTO MENSAL
1    |Poupança             |3%
2    |Fundos de renda fixa |4%'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

print("whats type of investiment? ")
print("1 - savings")
print("2 - fixed income")
number = int(input())
value = float(input("Value: R$"))

if(number == 1):
    value = value * 1.03
else:
    value = value * 1.04

print(f"Your return will be {value:.2f}")