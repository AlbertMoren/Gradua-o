'''Faça um programa que preencha uma matriz 20 X 10 com números inteiros, e some cada uma das colunas, armazenando o resultado da soma em um vetor. A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da coluna e mostrar a matriz resultante.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

from random import randint

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(20,10,0)
mat_result = []
coluna_soma = []
for i in range(len(mat)):                       #Preenchendo a matriz
    for j in range(len(mat[i])):
        mat[i][j] = randint(0,100)

for i in range(len(mat[i])):                       #Aplicando as regras de negocios
    soma =  0                      
    for j in range(len(mat)):
        soma+=mat[j][i]
    coluna_soma.append(soma)

for i in range(len(mat[i])):
    linha = []                       #Preenchendo a matriz
    for j in range(len(mat)):
        linha.append(mat[j][i]*coluna_soma[i])
    mat_result.append(linha)


for linha in mat_result:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:0} |",end=' ')
    print("")