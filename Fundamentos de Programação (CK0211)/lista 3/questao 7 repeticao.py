'''Faça um programa que receba a idade, a altura e o peso de cinco pessoas, calcule e mostre:
■ a quantidade de pessoas com idade superior a 50 anos;
■ a média das alturas das pessoas com idade entre 10 e 20 anos;
■ a porcentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas.'''
idade_cont = 0
altura_cont = 0.0
peso_cont =0
for i in range(5):
    idade,alt,peso = input("Insira a idade, altura e peso em seguida: ").split(" ")
    idade = int(idade)
    alt = float(alt)
    peso = float(peso)
    if(idade > 50):
        idade_cont+=1
    if(idade>10 and idade<20):
        altura_cont+=alt
    if(peso < 40):
        peso_cont+=1
media_alt = altura_cont/5
print(f"Tem um total de {idade_cont} pessoas superior a 50\nA media de altura com pessoas com idade de 10 a 20 anos é de {media_alt:.2f}\nTemos um total de {(peso_cont/5)*100:.0f}% pessoas com menos de 40kg")