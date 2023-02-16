'''Faça uma sub-rotina que receba como parâmetro o raio de uma esfera, calcule e mostre no programa principal o seu volume: v = 4/3 * R3.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(raio):
    volume = (4/3)*3.14*(raio**3)
    return volume

raio = float(input("Insira o raio da esfera: "))
print(F"O volume da esfera é {sub_rotina(raio):.2f}")