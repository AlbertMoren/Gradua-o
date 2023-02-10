'''Faça um programa que receba:
■ as notas de 15 alunos em cinco provas diferentes e armazene-as em uma matriz 15 x 5;
■ os nomes dos 15 alunos e armazene-os em um vetor de 15 posições.
O programa deverá calcular e mostrar:
■ para cada aluno, o nome, a média aritmética das cinco provas e a situação (aprovado, reprovado
ou exame);
■ a média da classe'''

from random import uniform

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(15,5,0)
nomes = ["alb","ert","sss","ggg","bbb","ccc","dd","ttt","ooo","xxx","zzz","hhh","qqqq","dddd","aaaa"]
medias = []
status = []

for i in range(len(mat)):
    soma = 0                       #Preenchendo a matriz
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0,10)
        soma+=mat[i][j]
    medias.append(soma/5)
    if medias[i] >= 7:
        status.append("Aprovado")
    elif medias[i] >= 5 and medias[i] < 7:
        status.append("AF")
    else:
        status.append("Reprovado")

                        
for i in range(len(medias)):                               #Imprimir a matriz na tela
    print(f"Aluno {nomes[i]:2} teve uma media {medias[i]:.1f} e está {status[i]}")