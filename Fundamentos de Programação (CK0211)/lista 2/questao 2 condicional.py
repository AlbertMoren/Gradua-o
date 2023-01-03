#Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra na tabela a seguir:

n1,n2 = input("Insira as 2 notas do aluno: ").split(" ")
n1 = float(n1)
n2 = float(n2)
media = (n1+n2)/2
if(media >=0 and media<3):
    print("Reprovado")
elif(media >= 3 and media < 7):
    print("Exame")
else:
    print("Aprovado")