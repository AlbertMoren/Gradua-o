'''Faça um programa que receba o preço de um produto e seu código de origem e mostre sua procedência. A procedência obedece à tabela a seguir.

CÓDIGO DE ORIGEM    |PROCEDÊNCIA
1                   |Sul
2                   |Norte
3                   |Leste
4                   |Oeste
5 ou 6              |Nordeste
7 ou 8 ou 9         |Sudeste
10 a 20             |Centro-oeste
21 a 30             |Nordeste'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

price = float(input("Enter product price: "))
code = int(input("Enter the product code:"))

if(code < 5 ):
    if(code == 1):
        print("the process of this product is from south")
    elif(code == 2):
        print("the process of this product is from north")
    elif(code == 3):
        print("the process of this product is from east")
    elif(code == 4):
        print("the process of this product is from west")
else:
    if(code == 5 or code ==6):
        print("the process of this product is from north east")
    elif(code >= 7 and code <=9):
        print("the process of this product is from southeast")
    elif(code >= 10 and code <=20):
        print("the process of this product is from midwest")
    elif(code >= 21 and code <=30):
        print("the process of this product is north east")