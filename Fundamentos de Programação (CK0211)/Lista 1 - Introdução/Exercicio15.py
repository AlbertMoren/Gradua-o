'''João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar
multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de
João'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salario = float(input("Qual seu salario? "))
conta1 = float(input("Qual valor da sua primeira conta"))
conta2 = float(input("Qual valor da sua segunda conta"))

conta1 = conta1 * 1.02
conta2 = conta2 * 1.02
salario = salario - (conta1 + conta2)

print(f"Vai resta R${salario:.2f} do salario")