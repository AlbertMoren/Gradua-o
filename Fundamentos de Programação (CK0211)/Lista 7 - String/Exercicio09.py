'''Make a program that takes a sentence and a character and checks whether the character entered is found in the sentence or not, and if it is found, how many times it happens.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina_contabilizar(text,caracter):
    lista= list(text)
    indice =0
    if caracter in lista:
        for i in range(len(lista)):
            if lista[i] == caracter:
                indice = i
                break
    else:
        indice = -1
    return indice

texto = input("Insira um texto: ").lower()
caracteres = input("Insira um texto: ").lower()
valor = sub_rotina_contabilizar(texto,caracteres)
if valor >=0:
    print(f"O '{caracteres}' se encontra na posição {valor+1} nessa na frase")
else:
    print(f"O caracater {caracteres} não aparece na frase")