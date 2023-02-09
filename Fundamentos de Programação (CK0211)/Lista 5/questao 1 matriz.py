from random import randint
'''Faça um programa que preencha uma matriz 3 X 5 com números inteiros, calcule e mostre a quantidade de elementos entre 15 e 20'''
#Função que gera uma matriz
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        # coloque linha na matriz
        matriz.append(linha)	
    return matriz

mat = crie_matriz(3,5,0)
cont = 0

for i in range(len(mat)):   #Valida a regra de negocio
    for j in range(len(mat[i])):
        mat[i][j] = randint(10,25)
        if mat[i][j] > 15 and mat[i][j] < 20:
            cont+=1
            
print(mat)
print(f"Tem {cont} elementos entre 15 e 20")