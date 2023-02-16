'''Faça um programa que receba uma frase e gere uma nova, retirando os espaços excedentes no início e no fim da frase e entre suas palavras.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(texto):
    lista = list(texto)
    lista1 = []
    for i in range(len(lista)):
        if lista[i] != " ":
            lista1.append(lista[i])
    texto = "".join(lista1)
    print(texto)

#Main
texto = input("Insira um texto: ").lower()
sub_rotina(texto)