'''Faça um programa que receba dez números inteiros e armazene-os em um vetor. Calcule e mostre dois vetores resultantes: o primeiro com os números pares e o segundo, com os números ímpares.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

vectorMain = [0]*10
vectorOdd = []
vectorPair = []

for i in range(10):
    vectorMain[i] = int(input("Enter number: "))

for i in range(10):
    if vectorMain[i]%2==0:
        vectorPair.append(vectorMain[i])
    else:
        vectorOdd.append(vectorMain[i])

print(f"the even values are {vectorPair}\nThe odd valeus are {vectorOdd}")