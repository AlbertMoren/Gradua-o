'''Crie um programa que preencha uma matriz 5 X 5 com números inteiros, calcule e mostre a soma:
■ dos elementos da linha 4;
■ dos elementos da coluna 2;
■ dos elementos da diagonal principal;
■ dos elementos da diagonal secundária;
■ de todos os elementos da matriz'''

from random import randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(5,5,0)
soma_linha_4 = 0
soma_coluna_2 = 0
soma_diagonal_principal = 0
soma_diagonal_segundaria = 0
total = 0

for i in range(len(mat)):                       #Preenchendo a matriz 1
    for j in range(len(mat[i])):
        mat[i][j] = randint(0,10)
        total+=mat[i][j]


for linha in mat:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:3} |",end=' ')
    print("")

for i in range(len(mat)):
    soma_linha_4+=mat[3][i]

for i in range(len(mat)):
    soma_coluna_2+=mat[i][1]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            soma_diagonal_principal+=mat[i][j]

for i in range(len(mat)):
    soma_diagonal_segundaria+=mat[i][5-1-i]

print(f"A soma total dos valores da matriz é {total}\nA soma da linha 4 = {soma_linha_4}\nA soma da coluna 2 = {soma_coluna_2}\nA soma da diagonal príncipal = {soma_diagonal_principal}\nA soma da diagonal segúndaria = {soma_diagonal_segundaria}")