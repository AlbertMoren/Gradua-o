'''Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e C — castanho) e a cor dos cabelos (P — preto; C — castanho; L — louro; e R — ruivo) de seis pessoas, e que calcule e mostre:
■ a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
■ a média das idades das pessoas com altura inferior a 1,50 m;
■ a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
■ a quantidade de pessoas ruivas e que não possuem olhos azuis.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

cont_idade_peso = 0
cont_idade_alt = 0
cont_olhos_azuis = 0
cont_ruivas_olhos = 0
for i in range(6):
    idade,alt,peso = input("Insira a idade, altura e peso em seguida: ").split(" ")
    idade = int(idade)
    alt = float(alt)
    peso = float(peso)
    olhos, cabelos = input("Cor dos Olhos, A,P,V,C e cor do cabelo O,C,L,R").split(" ")
    if(idade>50 and peso<60):
        cont_idade_peso+=1
    if(alt < 1.50):
        cont_idade_alt+=idade
    if(olhos == 'A'):
        cont_olhos_azuis+=1
    if(cabelos=='R' and olhos!='A'):
        cont_ruivas_olhos+=1
media_alt = cont_idade_alt/6
print(f"{cont_idade_peso} com 60 anos e menor de 60KG\n{media_alt:.2f} é a media de idade menor que 1,50 altura\n{(cont_olhos_azuis/6)*100:.0f}% pessoas com olhos azuis\n{cont_ruivas_olhos} pessoas ruivas com olhos não azuis")