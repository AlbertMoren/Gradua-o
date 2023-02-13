'''Faça uma sub-rotina que receba um valor inteiro e positivo, calcule e mostre seu fatorial'''

def sub_rotina(fat):
    if fat == 1:
        return fat
    else:
        return fat * sub_rotina(fat-1)

numero = int(input("Insira um valor: "))
print(f"O fatorial de {numero} = {sub_rotina(numero)}")