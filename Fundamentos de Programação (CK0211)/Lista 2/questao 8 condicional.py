'''Faça um programa para calcular e mostrar o salário reajustado de um funcionário. O percentual de aumento encontra-se na tabela a seguir. SALÁRIO PERCENTUAL DE AUMENTO Até R$ 300,00 35% Acima de R$ 300,00 15%'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salario = float(input("Qual o salario: R$"))
if(salario <= 300):
    print(f"Seu novo salário séra de {(salario + (salario*0.35)):.2f}")
else:
    print(f"Seu novo salário séra de {(salario + (salario*0.15)):.2f}")