'''Faça um programa que receba dez idades, pesos e alturas, calcule e mostre:
■ a média das idades das dez pessoas;
■ a quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro; e
■ a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de
1,90 m'''
cont_idade = 0
cont_alt = 0
cont_geral = 0
for i in range(10):
    idade,alt,peso = input("Insira a idade, altura e peso em seguida: ").split(" ")
    idade = int(idade)
    alt = float(alt)
    peso = float(peso)
    cont_idade+=idade
    if(peso>90 and alt<1.5):
        cont_alt+=1
    if(idade>10 and idade<30):
        if(alt>1,90):
            cont_geral+=1
media = cont_idade/10
print(f"{media:.2f} é a media das idades\n{cont_alt} é a qtd acima de 90kg\n{(cont_geral/10)*100:.0f}% de pessoas no 3º caso")
    