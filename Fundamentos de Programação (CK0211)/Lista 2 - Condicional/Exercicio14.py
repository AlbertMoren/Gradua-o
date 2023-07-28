'''Faça um programa que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre o novo salário 
FAIXA SALARIAL        |% DE AUMENTO
Até R$ 300,00         |50%
R$ 300,00 R$ 500,00   |40%
R$ 500,00 R$ 700,00   |30%
R$ 700,00 R$ 800,00   |20%
R$ 800,00 R$ 1.000,00 |10%
Acima de R$ 1.000,00  |5%'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salary = float(input("enter your salary: R$"))

if(salary <= 300):
    salary = salary * 1.5
elif(salary>300 and salary<=500):
    salary = salary * 1.4
elif(salary>500 and salary<=700):
    salary = salary * 1.3
elif(salary>700 and salary<=800):
    salary = salary * 1.2
elif(salary>800 and salary<=1000):
    salary = salary * 1.1
else:
    salary = salary * 1.05

print(f"Your new salay well be {salary:.2f}")