#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
#que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
#salário final.
salario_fixo = float(input("Valor do sálario fixo: R$"))
venda = float(input("Total de vendas: R$"))
salario_final = salario_fixo + (venda * 0.04)
print(f"Salário final dele séra de R${salario_final}")