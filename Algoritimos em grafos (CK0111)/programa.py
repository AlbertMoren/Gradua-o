#!/usr/bin/env python3
import fileinput
import sys

n = None
# Processar a entrada
for i, line in enumerate(fileinput.input()):
    if i == 2:  # Se for a terceira linha (índice 2)
        n = int(line.split('=')[1])  # Obtém o valor de n e converte para inteiro
        lista_de_adejacencia = [[] for _ in range(n)]
    elif i >= 4:  # Se for a partir da quinta linha (índice 4 em diante)
        # Fazer o processamento aqui
        v1 , v2 = map(int, line.strip().split())
        lista_de_adejacencia[v1-1].append(v2-1)
        lista_de_adejacencia[v2-1].append(v1-1)
        #Verfica se o verticia 1 nunca atigiu alguem, se for verdade, entao em sua lista ele recebe o valor do veritici 2
        
visitados = [-1]*n
componentes = []

for i in range(n):
    if visitados[i] == -1:
        componente = []
        stack = [i]
        while(stack):
            v = stack.pop()
            if visitados[v] == -1:
                visitados[v] = 1
                componente.append(v+1)
                for u in lista_de_adejacencia[v]:
                    stack.append(u)
        componentes.append(componente)

for i in range(n):
    if visitados == -1:
        componentes.append(i+1)
    
for componente in componentes:
    print(' '.join(str(v)for v in sorted(componente)))
             
sys.stdout.flush()  # Garantir que toda a saída seja escrita
