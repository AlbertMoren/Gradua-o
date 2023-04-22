#!/usr/bin/env python3
import fileinput
import sys

def main():
    # Abrir o arquivo de entrada e obter o número de vértices e a lista de adjacências
    n, lista_de_adejacencia =  abrirArquivoDeEntrada()
    # Realizar a busca em profundidade nos vértices e obter os vértices encontrados e visitados
    encontrados, visitados = DFS(n,lista_de_adejacencia)
    # Procurar vértices não visitados e adicioná-los à lista de vértices encontrados
    encontrados = procurarNãoVisitados(encontrados,n,visitados)
    # Imprimir os vértices encontrados no arquivo de saída
    imprimirNoAquivo(encontrados)

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

#Função responsavel por parti de um vertici qualquer e encontra todos os vizinhos dele
def DFS(n,lista_de_adejacencia):        
    #Marca todos os verticis como não visitados
    visitados = [-1]*n
    #Salva todos os verticis encontrado por sub_lista(Resposta do problema)
    encontrados = []

    for i in range(n):
        #Se nunca foi visitado, faça
        if visitados[i] == -1:
            #Vetor que irar salvar os verticis que percente ao um conjuto maximal do vertici de partida
            vertice = []
            #declara um vetor que simula uma pilha
            stack = [i]
            while(stack):
                v = stack.pop()
                if visitados[v] == -1:
                    #marca como verticis visitado
                    visitados[v] = 1
                    vertice.append(v+1)
                    for u in lista_de_adejacencia[v]:
                        stack.append(u)
            #Adiciona a lista de verticis encontrados em uma outra lista
            encontrados.append(vertice)
    return encontrados, visitados

#Função que busca os verticis isolados
def procurarNãoVisitados(encontrados,n,visitados):
    for i in range(n):
        if visitados[i] == -1:#Quer dizer que esse vertici nunca foi encontrado
            encontrados.append(i+1)
    return encontrados
    
def imprimirNoAquivo(encontrados):
    for encontrado in encontrados:
        print(' '.join(str(v)for v in sorted(encontrado)))            
    sys.stdout.flush()  # Garantir que toda a saída seja escrita

#Estarta todo o codigo
if __name__ == "__main__":
    main()