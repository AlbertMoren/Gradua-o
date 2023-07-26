'''Elabore uma sub-rotina que leia um número não determinado de valores positivos e retorne a média aritmética desses valores. Terminar a entrada de dados com o valor zero'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(list):
    media = sum(list)/len(list)
    return media


numero = []
while(True):
    number = int(input("Insira um valor: "))
    if number == 0:
        break
    numero.append(number)

med = sub_rotina(numero)
print(f"A media dos valores inseridos é {med:.1f}")