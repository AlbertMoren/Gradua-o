#Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha
#do usuário.
#ESCOLHA DO USUÁRIO     OPERAÇÃO
#   1                   Média entre os números digitados
#   2                   Diferença do maior pelo menor
#   3                   Produto entre os números digitados
#   4                   Divisão do primeiro pelo segundo

n1,n2 = input("Digite dois números: ").split(" ")
n1 = float(n1)
n2 = float(n2)
print("Qual operação deseja?\n1 - Média\n2 - diferença\n3 - Produto\n4 - divisão")
escolha = int(input())
if(escolha == 1):
    print(f"A media é {(n1+n2)/2}")
elif(escolha == 2):
    if(n1 > n2):
        print(f"A diferença é {n1-n2}")
    else:
        print(f"A diferença é {n2-n1}")
elif(escolha == 3):
    print(f"O produto é {n1*n2}")
elif(escolha == 4):
    print(f"A divisão é {n1/n2}")
else:
    print("ERRO")
    
