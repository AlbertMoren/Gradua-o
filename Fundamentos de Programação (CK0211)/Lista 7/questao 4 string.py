'''Faça um programa que receba uma frase, calcule e mostre a quantidade de palavras da frase digitada. Antes de contar a quantidade de palavras da frase, esta deverá passar pelas seguintes correções:
a) Eliminação de espaços no início da frase.
b) Eliminação de espaços no fim da frase.
c) Eliminação de espaços duplicados entre palavras.'''

def sub_rotina_editar(texto):
    lista = list(texto)
    lista1 = []
    last = lista[-1]
    for i in range(len(lista)):
        if lista[i] != ' ' or last != ' ':
           lista1.append(lista[i]) 
           last = lista[i]
    texto = "".join(lista1)
    return texto

def sub_rotina_contabilizar(texto):
    lista = list(texto)
    cont = 0
    for i in range(len(lista)):
        if lista[i] == " ":
            cont+=1
    return cont+1

#Main
texto = input("Insira um texto: ").lower()
texto = sub_rotina_editar(texto)
print(f"Essa frase contém {sub_rotina_contabilizar(texto)} palavras")