'''Faça um programa que preencha um vetor com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor'''

vetor = [0]*10
cont = 0
soma = 0
for i in range(len(vetor)):
    vetor[i] = int(input("Insira número negativos ou positivos: "))
    if vetor[i] < 0:
        cont += 1
    else:
        soma+=vetor[i]
