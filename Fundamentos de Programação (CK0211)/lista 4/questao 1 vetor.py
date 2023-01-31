'''Faça um programa que preencha um vetor com seis elementos numéricos inteiros. Calcule e mostre:
■ todos os números pares;
■ a quantidade de números pares;
■ todos os números ímpares;
■ a quantidade de números ímpares'''
vetor_geral = []
vetor_par =[]
cont_par = 0
vetor_impar = []
cont_impar = 0
for i in range(6):
    numero = int(input("número: "))
    vetor_geral.append(numero)
for i in range(len(vetor_geral)):
    if(vetor_geral[i]%2==0):
        vetor_par.append(vetor_geral[i])
        cont_par+=1
    else:
        vetor_impar.append(vetor_geral[i])
        cont_impar+=1
print(f"temos um total de {cont_par} pares, que sao {vetor_par}\nTemos um total de {cont_impar} ímpares, são eles {vetor_impar}")