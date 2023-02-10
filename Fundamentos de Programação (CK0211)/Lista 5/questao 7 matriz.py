'''Elabore um programa que preencha uma matriz M de ordem 4 X 6 e uma segunda matriz N de ordem 6 X 4, calcule e imprima a soma das linhas de M com as colunas de N.'''
from random import randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat1 = crie_matriz(4,6,0)
soma_colunas = []
soma_linhas = []
vet = []

for i in range(len(mat1)):                       #Preenchendo a matriz 1
    for j in range(len(mat1[i])):
        mat1[i][j] = randint(0,100)

mat2 = crie_matriz(6,4,0)

for i in range(len(mat2)):                       #Preenchendo a matriz 2
    for j in range(len(mat2[i])):
        mat2[i][j] = randint(0,100)


for i in range(len(mat1)):                       #Somando as linhas
    soma = 0
    for j in range(len(mat1[i])):
        soma+=mat1[i][j]
    soma_linhas.append(soma)

for i in range(len(mat2[i])):                     #Somando as colunas
    soma = 0
    for j in range(len(mat1)):
        soma+=mat1[j][i]
    soma_colunas.append(soma)

for i in range(len(soma_linhas)):                  #Somando as colunas e as linhas
    vet.append(soma_linhas[i]+soma_colunas[j])

for valor in vet:
    print(f"{valor:2} ",end='')