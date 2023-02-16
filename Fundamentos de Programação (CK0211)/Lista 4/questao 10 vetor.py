''' Faça um programa que preencha um vetor com dez números inteiros e um segundo vetor com cinco números inteiros, calcule e mostre dois vetores resultantes. O primeiro vetor resultante será composto pela soma de cada número par do primeiro vetor somado a todos os números do segundo vetor. O segundo vetor resultante será composto pela quantidade de divisores que cada número ímpar do primeiro vetor tem no segundo vetor'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

vetor1 = [0]*10
vetor2 = [0]*5
vetor_result1 = []
vetor_result2 = []
cont = 0

print("Preencher vetor 1")
for i in range(len(vetor1)):
    vetor1[i] = int(input(f"elemento {i+1}º: "))

print("\nPreencher vetor 2")
for i in range(len(vetor2)):
    vetor2[i] = int(input(f"elemento {i+1}º: "))


for i in range(len(vetor1)):
    if vetor1[i] % 2 == 0:
        vetor_result1.append( vetor1[i] + sum(vetor2))
    else:
        cont = 0
        for j in range(len(vetor2)):
            if vetor1[i] % vetor2[j] == 0:
                cont+= 1
        vetor_result2.append(cont)

print(f"{vetor_result1}\n{vetor_result2}")