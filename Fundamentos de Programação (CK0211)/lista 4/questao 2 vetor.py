''' Faça um programa que preencha um vetor com sete números inteiros, calcule e mostre:
■ os números múltiplos de 2;
■ os números múltiplos de 3;
■ os números múltiplos de 2 e de 3'''
vetor_geral = []
vetor_2 =[]
vetor_3 = []
vetor_2e3 = []
for i in range(6):
    numero = int(input("número: "))
    vetor_geral.append(numero)
for i in range(len(vetor_geral)):
    if(vetor_geral[i]%2==0 and vetor_geral[i]%3==0):
        vetor_2e3.append(vetor_geral[i])
    elif(vetor_geral[i]%2==0):
        vetor_2.append(vetor_geral[i])
    elif(vetor_geral[i]%3==0):
        vetor_3.append(vetor_geral[i])
print(f"Números múltiplos por 2 são {vetor_2}\nNúmeros múltiplos por 3 são {vetor_3}\nNúmeros Mutiplos por 2 e 3 são {vetor_2e3}")
