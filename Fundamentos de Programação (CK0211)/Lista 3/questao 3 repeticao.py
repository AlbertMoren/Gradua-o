'''Faça um programa que receba a idade de oito pessoas, calcule e mostre:
a) a quantidade de pessoas em cada faixa etária;
b) a porcentagem de pessoas na primeira faixa etária com relação ao total de pessoas.
c) a porcentagem de pessoas na última faixa etária com relação ao total de pessoas
FAIXA ETÁRIA IDADE
1a Até 15 anos
2a De 16 a 30 anos
3a De 31 a 45 anos
4a De 46 a 60 anos
5a Acima de 60 anos'''
faixa1 = 0
faixa2  = 0
faixa3  = 0
faixa4  = 0
faixa5 = 0
for i in range(8):
    idade = int(input("Idade: "))
    if(idade <= 15):
        faixa1 += 1
    elif(idade>15 and idade<=30):
        faixa2+=1
    elif(idade>30 and idade<=45):
        faixa3+=1
    elif(idade>45 and idade<=60):
        faixa4+=1
    else:
        faixa5+=1
print(f"Existe {(faixa1/8)*100:.0f}% da faixa1\nExiste {(faixa5/8)*100:.0f}")
    