'''Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e mostre-os na ordem lida. Em seguida, organize-os em ordem crescente e decrescente'''
#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

for i in range(4):
    num1, num2,num3,num4 = input("Insira 4 valores: ").split(" ")
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    print(f"Grupo {i}\nPela ordem lida\n{num1}-{num2}-{num3}-{num4}") 
    if(num1 > num2):
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    if(num3 > num4):
        maior1 = num3
        menor1 = num4
    else:
        maior1 = num4
        menor1 = num3
    if(maior < maior1):
        aux = maior
        maior = maior1
        maior1 = aux
    if(menor > menor1):
        aux = menor
        menor = menor1
        menor1 = aux
    if(maior1 < menor1):
        aux = maior1
        maior1 = menor1
        menor1 = aux
    print(f"Em ordem descrecente\n{menor}-{menor1}-{maior1}-{maior}\nEm Ordem Crescente\n{maior}-{maior1}-{menor1}-{menor}")

        