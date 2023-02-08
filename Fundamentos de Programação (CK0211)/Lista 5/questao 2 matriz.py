'''Crie um programa que preencha uma matriz 2 X 4 com números inteiros calcule e mostre:
■ a quantidade de elementos entre 12 e 20 em cada linha;
■ a média dos elementos pares da matriz'''
from random import randint
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        # coloque linha na matriz
        matriz.append(linha)	
    return matriz

mat = crie_matriz(2,4,0)

for i in range(mat):
    for j in range(mat[i]):
        mat[i][j] = randint(0,25)


for i in range(mat):
    for j in range(mat[i]):
        