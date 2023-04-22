#!/usr/bin/env python3
import fileinput
import sys

# Processar a entrada
for line in fileinput.input():
    # Fazer o processamento aqui
    print(line.rstrip())  # Exemplo: imprimir a linha de entrada sem o caractere de nova linha

# Escrever a saída
sys.stdout.flush()  # Garantir que toda a saída seja escrita


#comandop ara execultar no terminal do linux
# cat 0.in | ./grafo.py >saida.txt

#comandop ara execultar no terminal do windons
# Get-Content 0.in | python grafo.py > saida.txt