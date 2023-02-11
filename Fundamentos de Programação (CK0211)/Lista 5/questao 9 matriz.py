'''Faça um programa que preencha uma matriz 3 x 3 com números reais e outro valor numérico digitado pelo usuário. O programa deverá calcular e mostrar a matriz resultante da multiplicação do número digitado por cada elemento da matriz.'''
from random import uniform,randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(3,8,0)
mat_result =[]

for i in range(len(mat)):                       #Preenchendo a matriz 1
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0,100)

numero = randint(1,100)

for i in range(len(mat)):                       #mutiplicando os elementos da matriz por um unico valor
    linha = []
    for j in range(len(mat[i])):
        linha.append(mat[i][j]*numero)
    mat_result.append(linha)

for linha in mat_result:                                #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:.1f} |",end=' ')
    print("")