'''Faça um programa que apresente o menu de opções a seguir:
Menu de opções:
1. Média aritmética
2. Média ponderada
3. Sair
Digite a opção desejada.
Na opção 1: receber duas notas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada.
Na opção 3: sair do programa
Verifique a possibilidade de opção inválida. Nesse caso, o programa deverá mostrar uma mensagem.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

while True:
    print("1 - Arithmetic average")
    print("2 - Weighted everage")
    print("3 - Exit")
    choice = int(input())
    if choice == 1:
        noteOne = float(input("Enter the first note: "))
        noteTwo = float(input("Enter the second note: "))
        everage = (noteOne + noteTwo)/2
        print(f"The everage of these scores is {everage:.2f}")
    elif choice == 2:
        noteOne = float(input("Enter the first note: "))
        weightOne = int(input("You weight: "))
        noteTwo = float(input("Enter the second note: "))
        weightTwo = int(input("You weight: "))
        noteThree = float(input("Enter the second note: "))
        weightThree = int(input("You weight: "))
        everage = ((noteOne*weightOne)+(noteTwo*weightTwo)+(noteThree*weightThree))/(weightOne+weightTwo+weightThree)
        print(f"The everage of these scores is {everage:.2f}")
    elif choice == 3:
        break
    else:
        print("invalid option, try again ")