#Faça um programa que receba dois números e execute uma das operações listadas a seguir, de acordo com a
#escolha do usuário. Se for digitada uma opção inválida, mostre mensagem de erro e termine a execução do
#programa. As opções são:
#a) O primeiro número elevado ao segundo número.
#b) Raiz quadrada de cada um dos números.
#c) Raiz cúbica de cada um dos números.

n1,n2 = input("Digite dois números: ").split(" ")
n1 = float(n1)
n2 = float(n2)
print("Qual operação deseja?\n1 - O primeiro elevado ao segundo número\n2 - raiz quadrada de cada\n3 - raiz cúbica de cada")
escolha = int(input())
if(escolha == 1):
    print(f"O primeiro elevado ao segundo é {n1 ** n2}")
elif(escolha == 2):
    print(f"Raiz quadrada do {n1} é {n1 ** 0.5:.2f} e do {n2} é {n2 ** 0.5:.2f}")
elif(escolha == 3):
    print(f"A raiz cúbica do {n1} é {n1 ** (1/3):.2f} e do {n2} é {n2 ** (1/3):.2f}")
else:
    print("ERRO")