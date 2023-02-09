'''Elabore um programa que preencha uma matriz 6 X 3, calcule e mostre:
■ o maior elemento da matriz e sua respectiva posição, ou seja, linha e coluna;
■ o menor elemento da matriz e sua respectiva posição, ou seja, linha e coluna.'''

from random import randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(6,3,0)
maior,linha_maior,coluna_maior  = 0,0,0
menor,linha_menor,coluna_menor  = 0,0,0

for i in range(len(mat)):                       #Preenchendo a matriz
    for j in range(len(mat[i])):
        mat[i][j] = randint(0,30)
        if i==0 and j==0:
            menor = mat[i][j]
        if mat[i][j] < menor:
            menor = mat[i][j]
            linha_menor = i
            coluna_menor = j
        if mat[i][j] > maior:
            maior = mat[i][j]
            linha_maior = i
            coluna_maior = j

for linha in mat:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:3} |",end=' ')
    print("")
    
print(f"O maior elemento fica na linha {linha_maior+1} coluna {coluna_maior+1} e é o valor {maior}\nO menor elemento fica na linha {linha_menor+1} coluna {coluna_menor+1} e é o valor {menor}")

    