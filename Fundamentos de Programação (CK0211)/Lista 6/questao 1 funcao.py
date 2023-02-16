'''Faça uma sub-rotina que receba um número inteiro e positivo N como parâmetro e retorne a soma dos números inteiros existentes entre o número 1 e N (inclusive).'''
#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def func(n):
    soma=0
    for i in range(n+1):
        soma+=i
    return soma

n = int(input("Insira um número: "))
soma = func(n)
print(f"{soma}")