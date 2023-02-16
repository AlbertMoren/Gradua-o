'''Faça um programa que receba uma frase e gere uma nova frase, duplicando cada caractere da frase digitada. Exemplo:
Frase: PROGRAMAR É BOM
Saída: PPRROOGGRRAAMMAARR ÉÉ BBOOMM'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina_editar(text):
    lista = list(text)
    lista1= []
    for i in range(len(lista)):
        caracter = lista[i]
        if caracter == " ":
            lista1.append(caracter)
        else:
            for j in range(2):
                lista1.append(caracter)
    text = "".join(lista1)
    return text

#Main
texto = input("Insira um texto: ").lower()
texto = sub_rotina_editar(texto)
print(texto)