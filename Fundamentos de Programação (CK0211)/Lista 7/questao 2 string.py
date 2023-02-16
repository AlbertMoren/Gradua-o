'''Faça um programa que receba uma frase e mostre cada palavra dela em uma linha separada. Exemplo:
Frase: COMPUTADORES SÃO MÁQUINAS POTENTES
Saída:
COMPUTADORES
SÃO
MÁQUINAS
POTENTES'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(texto):
    for i in range(len(texto)):
        if texto[i] != ' ':
            print(texto[i],end="")
        else:
            print("")

#Main
texto = input("Insira um texto: ").lower()
sub_rotina(texto)