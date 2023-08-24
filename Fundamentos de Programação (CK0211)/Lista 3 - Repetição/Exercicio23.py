'''Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade de opção inválida e não se preocupe com as restrições como salário inválido.
Menu de opções:
1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair
Digite a opção desejada.
'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

while True:
    print("1 - New salary")
    print("2 - Vacation ")
    print("3 - Thirteenth")
    print("4 - Exit")
    choice = int(input())
    if choice == 4:
        break
    elif choice == 1:
        salary = float(input("Enter your salary: "))
        if salary < 210:
            salary = salary * 1.15
        elif salary >= 210 and salary <= 600:
            salary = salary * 1.10
        else:
            salary = salary * 1.05
        print(f"Your new salary is {salary:.2f}")
    elif choice == 2:
        salary = float(input("Enter your salary: "))
        salary = salary * (1/3)
        print(f"Your vacation will be {salary:.2f}")
    elif choice == 3:
        salary = float(input("Enter your salary: "))
        months = int(input("how much months in the company: "))
        salary = (salary * months)/12
        print(f"Your thirteenth will be {salary:.2f}")
    else:
        print("invalid option. Try again")