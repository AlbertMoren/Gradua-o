'''Crie uma sub-rotina que receba como parâmetro dois valores X e Z, calcule e retorne X^Z sem utilizar funções ou operadores de potência prontos.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(x,z):
    if z == 1:
        return x
    else:
        return x * sub_rotina(x,z-1)

number1,number2 = input("Insira dois valor: ").split(" ")
number1= int(number1)
number2 = int(number2)
print(f" {number1} elevado a {number2}  = {sub_rotina(number1,number2)}")