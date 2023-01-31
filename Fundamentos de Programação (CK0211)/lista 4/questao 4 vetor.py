'''Faça um programa que preencha um vetor com quinze elementos inteiros e verifique a existência de elementos
iguais a 30, mostrando as posições em que apareceram.'''
lista = [0]*5
posicoes = []
for i in range(len(lista)):
    valor = int(input("Só vá inserindo valores: "))
    lista.insert(i,valor)
    if 0 in lista:
       lista.remove(0)                                  #Remove os 0 do vetor
for i in range(len(lista)):
    if(lista[i] == 30):
        posicoes.append(i)
if(len(posicoes) == 0):                                 #Impimi na tela caso tenha elemento 30 no vetor
    print("Não nenhum valor 30 no vetor")
else:
    print("Valores iguais a 30, estão nas posições",end="")
    for i in posicoes:
        print(f" {i+1}",end="")
