'''Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir, calcule e mostre o valor do aumento e o novo salário

SALÁRIO             |PERCENTUAL DE AUMENTO
Até R$ 300,00       | 15%
R$ 300,00 R$ 600,00 |10%
R$ 600,00 R$ 900,00 |5%
Acima de R$ 900,00  |0%'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salary = float(input("enter your salary: R$"))

if(salary <= 300.00):
    salary = salary * 1.15
elif(salary > 300.00 and salary<600.00):
    salary = salary * 1.10
elif(salary >= 600.00 and salary<=900.00):
    salary = salary * 1.05

print(f"Your new salay well be {salary:.2f}")