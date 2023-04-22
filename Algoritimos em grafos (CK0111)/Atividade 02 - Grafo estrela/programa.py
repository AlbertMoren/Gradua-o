#!/usr/bin/env python3
import fileinput
import sys

def main():
    # Abrir o arquivo de entrada e obter o número de vértices e a lista de adjacências
    n, lista_de_adejacencia =  abrirArquivoDeEntrada()
    # Procura se o grafo em questao é um grafo estrela
    estrela = grafoEstrela(n,lista_de_adejacencia)
    # Imprimir se é ou não um grafo estrela
    imprimirNoAquivo(estrela)

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

#Função que verifica se é um grafo estrela
def grafoEstrela(n,lista_de_adejacencia):
    estrela = False
    indicis = []
    cont = 0
    #Verifica os graus dos vertices
    for u in range(n):
        grau = 0
        for v in lista_de_adejacencia[u]:
            grau+=1
        indicis.append(grau)

    #Verifica se tem algum vertifica com n-1 arestas e todos os outros com somente uma aresta
    if n-1 in indicis:
        for v in indicis:
            if v == 1:
                cont+=1
        if cont == n-1:
            estrela = True
            
    return estrela
    
def imprimirNoAquivo(estrela):
    if estrela == True:
        print("È um grafo estrela")
    else:
        print("Não é um grafo estrela")
    sys.stdout.flush()  # Garantir que toda a saída seja escrita

#Estarta todo o codigo
if __name__ == "__main__":
    main()