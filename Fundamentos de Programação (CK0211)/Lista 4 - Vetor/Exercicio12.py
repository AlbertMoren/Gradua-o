'''Faça um programa que receba cinco números e mostre a saída a seguir:
Digite o 1º número 5
Digite o 2º número 3
Digite o 3º número 2
Digite o 4º número 0
Digite o 5º número 2
Os números digitados foram: 5 + 3 + 2 + 0 + 2 = 12'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

vectorMain = [0]*5

for i in range(5):
    vectorMain[i] = int(input("Enter number: "))

sum = sum(vectorMain)
exitWord = " + ".join(map(str,vectorMain))
print(f"The numbers entered were = {exitWord} = {sum}")
