'''Faça um programa para criptografar uma frase dada pelo usuário. Na criptografia, a frase deverá ser invertida e as consoantes deverão ser trocadas por #. Exemplo:
Frase: EU ESTOU NA ESCOLA
Saída: A#O##E A# UO##E UE'''
maiusculas = ('b','c','d','f','g','h','i','j','l','m','n','p','q','r','s','t','v','x','w','y','z')

def sub_rotina(texto):
    lista = list(texto)
    for i in range(len(lista)):
        for elemeto in maiusculas:
            if lista[i] == elemeto:
                lista[i] = '#'
    texto = "".join(lista)
    print(texto[::-1])

#Main
texto = input("Insira um texto: ").lower()
sub_rotina(texto)