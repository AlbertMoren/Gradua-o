# Faça um programa que receba três números e mostre o menor.
n1,n2,n3 = input("Insira as 3 números: ").split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
menor = n1
if(n2 < menor or n3< menor):
    if(n2 < n3):
        print(f"O {n2} é o menor de todos eles")
    else:
        print(f"O {n3} é o menor de todos eles")
else:
    print(f"O {menor} é o menor de todos eles")