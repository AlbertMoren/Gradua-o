'''Crie uma sub-rotina que receba como parâmetro um valor inteiro e positivo e retorne a soma dos divisores desse valor.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(numero,i):
    if i == numero:
        return numero
    else:
        if numero%i==0:
            return i + sub_rotina(numero,i+1)
        else:
            return sub_rotina(numero,i+1)

i = 1
numero = int(input("Insira um valor: "))
print(f"A soma dos valores dos div de  {numero} = {sub_rotina(numero,i)}")