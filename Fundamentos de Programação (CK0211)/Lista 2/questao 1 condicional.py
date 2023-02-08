#Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a
#mensagem de aprovado ou reprovado, considerando para aprovação média 7.

n1,n2,n3,n4 = input("Insira as 4 notas do aluno: ").split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1+n2+n3+n4)/4
if(media >= 7):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")