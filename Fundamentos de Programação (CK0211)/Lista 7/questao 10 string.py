'''Faça um programa que receba uma frase e um caractere e verifique em que posição da frase o caracteredigitado aparece pela última vez'''

def sub_rotina_contabilizar(text,caracter):
    lista= list(text)
    indices = []
    indice = -1
    last = 0
    if " " in lista:
        for i in range(len(lista)):
            if lista[i] == " ":
                indices.append(i)
        last = indices[-1]
        while(last != len(lista)):
            if lista[last] == caracter:
                indice = last
                break
            last+=1
    else:
        for i in range(lista):
            if lista[i] == caracter:
                indice = i
    return indice

#main
texto = input("Insira um texto: ").lower()
caracteres = input("Insira um texto: ").lower()
valor = sub_rotina_contabilizar(texto,caracteres)
if valor >=0:
    print(f"O '{caracteres}' se encontra na posição {valor+1} nessa na ultima palavra dessa frase")
else:
    print(f"O caracater {caracteres} não aparece na ultima palavra da frase")