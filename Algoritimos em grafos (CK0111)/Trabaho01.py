import fileinput
import sys
from queue import Queue

class No:
    def __init__(lista,dado):
        lista.valor = dado
        lista.proximo = None

class Lista:
    #Construtor da minha lista encadeada
    def __init__(lista):
        lista.primeiro = None
    
    #Função que inseri um valor na lista
    def inserir(lista,dado):
        novo_no = No(dado)
        if lista.primeiro == None:
            lista.primeiro = novo_no
            return
        no_atual = lista.primeiro
        while no_atual.proximo != None:  #Percorrendo a lista
            no_atual = no_atual.proximo
        no_atual.proximo = novo_no

    def imprimir(lista):
        no_atual = lista.primeiro
        while no_atual != None:
            print(no_atual.valor)
            no_atual = no_atual.proximo

indicis = [-1]*10
vetor_de_lista = [Lista() for i in range(10)]

# Processar a entrada
for line in fileinput.input():
    # Fazer o processamento aqui
    print(line.rstrip())  # Exemplo: imprimir a linha de entrada sem o caractere de nova linha

# Escrever a saída
sys.stdout.flush()  # Garantir que toda a saída seja escrita