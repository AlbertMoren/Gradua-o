#!/usr/bin/env python3
import fileinput
import sys

def main():
    # Abrir o arquivo de entrada e obter o número de vértices e a lista de adjacências
    n, lista_de_adejacencia =  abrirArquivoDeEntrada()
    # Realiza a conta do vertice com maior grau, e retorna esse mesmo vertice
    vm,gm = grauMaximo(n,lista_de_adejacencia)
    # Imprimir os vértices encontrados no arquivo de saída
    imprimirNoAquivo(vm,gm)

# Processar a entrada
def abrirArquivoDeEntrada():
    n = None
    for i, line in enumerate(fileinput.input()):
        if i == 2:  # verifica se é a linha 2
            n = int(line.split('=')[1])  # Obtém o valor de n e converte para inteiro
            lista_de_adejacencia = [[] for _ in range(n)] #Com base no 'N' anterior, declara uma lista de adjacencias
        elif i >= 4:  # A parti da linha 3, para trabalhar com os verticis
            v1 , v2 = map(int, line.strip().split())
            lista_de_adejacencia[v1-1].append(v2-1)
            lista_de_adejacencia[v2-1].append(v1-1)
    return n,lista_de_adejacencia

#Função responsavel para verificar com o maior grau dentre todos os verticis
def grauMaximo(n,lista_de_adejacencia):
    grauMaximo = -1
    indicis = list()
    verticeMaximo = list()

    for u in range(n):
        grau = 0
        for v in lista_de_adejacencia[u]:
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