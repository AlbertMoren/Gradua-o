'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1, 2, 3, 4 Votos para os respectivos candidatos
5 Voto nulo
6 Voto em branco
Faça um programa que calcule e mostre:
■ o total de votos para cada candidato;
■ o total de votos nulos;
■ o total de votos em branco;
■ a porcentagem de votos nulos sobre o total de votos; e
■ a porcentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos, tem-se o valor zero e, para códigos inválidos, o programa deverá mostrar uma mensagem.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

contNull = 0
contWhite = 0
contOne = 0
contTwo = 0
contThree = 0
contFour = 0


while True:
    candidate = int(input("Choice your candidade: "))
    if candidate == 0:
        break
    elif candidate == 1 or candidate == 2 or candidate==3 or candidate==4:
        if candidate == 1:
            contOne+=1
        elif candidate == 2:
            contTwo+=1
        elif candidate == 3:
            contThree+=1
        else:
            contFour
    elif candidate == 5:
        contNull+=1
    elif candidate == 6:
        contWhite +=1

print(f"candidade 1 had {contOne}\ncandidade 2 had {contTwo}\ncandidade 3 had {contThree}\ncandidade 4 had {contFour}\nNull votes were {contNull}\nWhite votes were {contWhite}")