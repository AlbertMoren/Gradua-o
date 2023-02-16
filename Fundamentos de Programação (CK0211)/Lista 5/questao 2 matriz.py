'''Crie um programa que preencha uma matriz 2 X 4 com números inteiros calcule e mostre:
■ a quantidade de elementos entre 12 e 20 em cada linha;
■ a média dos elementos pares da matriz'''
from random import randint

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(2,4,0)
soma = 0
linha1 = 0
linha2 = 0
cont1 = 0

for i in range(len(mat)):                       #Preenchendo a matriz
    for j in range(len(mat[i])):
        mat[i][j] = randint(0,25)

                        
for linha in mat:                               #Imprimir a matriz na tela
    print("|",end='')  
    for valor in linha:
        print(f" {valor:3} |",end=' ')
    print("")
    

for i in range(len(mat)):                       #Regras de negocio
    for j in range(len(mat[i])):
        if mat[i][j] % 2 == 0:
            soma+=mat[i][j]
            cont1+=1
        if i == 0:
            if mat[i][j]>12 and mat[i][j] <20:
                linha1+=1
        else:
            if mat[i][j]>12 and mat[i][j] <20:
                linha2+=1
    

print(f"A média dos elementos pares da matriz é {soma/cont1:.2f}\nElementos entre 12 e 20 temos o seguinte\nNa linha 1 = {linha1} e na linha 2 = {linha2}")