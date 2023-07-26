'''Faça um programa que receba uma frase e um caractere e verifique se o caractere digitado é encontrado na frase ou não e, se for encontrado, quantas vezes isso acontece.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina_contabilizar(text,caracter):
    lista= list(text)
    cont =0
    if caracter in lista:
        for i in range(len(lista)):
            if lista[i] == caracter:
                cont+=1
    return cont

texto = input("Insira um texto: ").lower()
caracteres = input("Insira um texto: ").lower()
valor = sub_rotina_contabilizar(texto,caracteres)
if valor >0:
    print(f"O '{caracteres}' se encontra {valor} vezes na frase")
else:
    print(f"O caracater {caracteres} não aparece na frase")