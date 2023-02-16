'''Faça um programa que receba uma frase e mostre quantas letras diferentes ela contém'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina_contabilizar(text):
    lista = list(text)
    lista1 = []
    cont = 0
    for i in range(len(lista)):
        if lista[i] in lista1:
            continue
        else:
            if lista[i] != " ":
                cont+=1
                lista1.append(lista[i])
    return cont

texto = input("Insira um texto: ").lower()
print(f"Essa frase tem {sub_rotina_contabilizar(texto)} caracteres diferentes")