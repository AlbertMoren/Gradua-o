'''Faça um programa que receba uma frase, calcule e mostre a quantidade de palavras da frase digitada. Antes de contar a quantidade de palavras da frase, esta deverá passar pelas seguintes correções:
a) Eliminação de espaços no início da frase.
b) Eliminação de espaços no fim da frase.
c) Eliminação de espaços duplicados entre palavras.'''

def sub_rotina(texto):
    lista = list(texto)
    lista1 = []
    cont = 0
    print(len(lista))
    for i in range(len(lista)):
        if i-1 == len(lista):
            break
        elif lista[i] != " " and lista[i+1] != " ":
            lista1.append(lista[i])
    texto = "".join(lista1)
    return texto


#Main
texto = input("Insira um texto: ").lower()
texto = sub_rotina(texto)
print(texto)