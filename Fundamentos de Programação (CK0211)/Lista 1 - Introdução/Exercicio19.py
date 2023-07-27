'''Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 W
de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre
a sua área (em m2) e a potência de iluminação que deverá ser utilizada.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

largura = float(input("Insira o valor da largura: "))
comprimento = float(input("Insira o valor da comprimento: "))

area = largura * comprimento

print(f"Vai ser necessário {area * 18}w para esse comodo")