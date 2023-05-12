#!/usr/bin/env python3
import fileinput
import sys

def main():
    # Abrir o arquivo de entrada e obter o número de vértices e a lista de adjacências
    n, matriz_de_adjacencia =  abrirArquivoDeEntrada()
    # Realiza a conta do vertice com maior grau, e retorna esse mesmo vertice
    vm,gm = grauMaximo(n,matriz_de_adjacencia)
    # Imprimir os vértices encontrados no arquivo de saída
    imprimirNoAquivo(vm,gm)


def criar_matriz(n, valor_inicial):
    matriz = []
    for _ in range(n):
        linha = [valor_inicial] * n
        matriz.append(linha)
    return matriz


# Processar a entrada
def abrirArquivoDeEntrada():
    n = None
    for i, line in enumerate(fileinput.input()):
        if i == 2:  # verifica se é a linha 2
            n = int(line.split('=')[1])  # Obtém o valor de n e converte para inteiro
            matriz_de_adjacencia = criar_matriz(n,-1) #Com base no 'N' anterior, declara uma lista de adjacencias
        elif i >= 4:  # A parti da linha 3, trabalhar com os verticis
            v1 , v2 = map(int, line.strip().split())
            matriz_de_adjacencia[v1-1][v2-1] = 1
            matriz_de_adjacencia[v2-1][v1-1] = 1
    return n,matriz_de_adjacencia

#Função responsavel para verificar com o maior grau dentre todos os verticis
def grauMaximo(n,matriz_de_adjacencia):
    grauMaximo = -1
    indicis = list()
    verticeMaximo = list()

    for u in range(n):
        grau = 0
        for v in matriz_de_adjacencia[u]:
            if (v == 1):
                grau+=1
        indicis.append(grau)
        if grau >= grauMaximo:
            grauMaximo = grau

    for u in range(len(indicis)):
        if indicis[u] == grauMaximo:
            verticeMaximo.append(u+1)
    #Retorna o grau maximo e os vertices com o mesmo grau
    return verticeMaximo,grauMaximo
    
def imprimirNoAquivo(verticeMaximo, grauMaximo):
    print(f"Os vertice(s) de grau {grauMaximo} que é o maximo. É o(s) ", end="")
    print(*verticeMaximo, sep=', ')         
    sys.stdout.flush()  # Garantir que toda a saída seja escrita

#Estarta todo o codigo
if __name__ == "__main__":
    main()