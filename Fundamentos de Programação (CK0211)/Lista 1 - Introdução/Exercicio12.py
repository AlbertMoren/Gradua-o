'''Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule
e mostre a quantidade de salários mínimos que esse funcionário ganha.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salarioMinimo = float(input("Informe o salario mínimo"))
salario = float(input("Informe o salario do funcionario"))

salarios = salario//salarioMinimo

print(f"São {salarios} salario minimo no salario desse funcionario")