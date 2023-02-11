'''Crie um programa que preencha duas matrizes 3 X 8 com números inteiros, calcule e mostre:
■ a soma das duas matrizes, resultando em uma terceira matriz também de ordem 3 X 8;
■ a diferença das duas matrizes, resultando em uma quarta matriz também de ordem 3 X 8'''

from random import randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat1 = crie_matriz(3,8,0)

for i in range(len(mat1)):                       #Preenchendo a matriz 1
    for j in range(len(mat1[i])):
        mat1[i][j] = randint(0,100)

mat2 = crie_matriz(3,8,0)

for i in range(len(mat2)):                       #Preenchendo a matriz 2
    for j in range(len(mat2[i])):
        mat2[i][j] = randint(0,100)

mat_rest_soma = []
for i in range(len(mat1)):                      #Soma as matrizes
    linha = []
    for j in range(len(mat1[i])):
        linha.append(mat1[i][j]+mat2[i][j])
    mat_rest_soma.append(linha)

for linha in mat_rest_soma:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:3} |",end=' ')
    print("")

print("="*60)

mat_rest_diferenca = []
for i in range(len(mat1)):                      #subtrair as matrizes
    linha = []
    for j in range(len(mat1[i])):
        if mat2[i][j] < 0:
            linha.append(mat1[i][j]-(-mat2[i][j]))
        else:
            linha.append(mat1[i][j]-mat2[i][j])
    mat_rest_diferenca.append(linha)

for linha in mat_rest_diferenca:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:3} |",end=' ')
    print("")