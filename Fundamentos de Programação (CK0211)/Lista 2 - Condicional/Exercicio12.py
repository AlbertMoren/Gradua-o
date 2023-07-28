'''Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

    TABELA DAS GRATIFICAÇÕES
SALÁRIO             |GRATIFICAÇÃO
Até R$ 350,00       |R$ 100,00
R$ 350,00 R$ 600,00 |R$ 75,00
R$ 600,00 R$ 900,00 |R$ 50,00
Acima de R$ 900,00  |R$ 35,00'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salary = float(input("enter your salary: R$"))


if(salary <= 350.00):
    salary = salary + 100
elif(salary > 350.00 and salary<600.00):
    salary = salary + 75
elif(salary >= 600.00 and salary<=900.00):
    salary = salary + 20
else:
    salary+= 35

salary = salary * 0.93

print(f"Your new salay well be {salary:.2f}")