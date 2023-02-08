'''Faça um programa que preencha três vetores com dez posições cada um: o primeiro vetor, com os nomes de dez produtos; o segundo vetor, com os códigos dos dez produtos; e o terceiro vetor, com os preços dos produtos. Mostre um relatório apenas com o nome, o código, o preço e o novo preço dos produtos que sofrerão aumento. Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código par ou preço superior a R$ 1.000,00. Sabe-se ainda que, para os produtos que satisfazem as duas condições anteriores, código e preço, o aumento será de 20%; para aqueles que satisfazem apenas a condição de código, o aumento será de 15%; e para aqueles que satisfazem apenas a condição de preço, o aumento será de 10%.'''

nome_produtos = []
id_produtos = [0]*3
precos_produtos = [0]*3
nome_produtos_att = []
id_produtos_att = []
precos_produtos_att = []


for i in range(len(id_produtos)):               #Inserção de valores nos vetores
    id_produtos[i] = int(input("Insira o ID do produto: "))
    if id_produtos[i] in id_produtos:   #Validar se o ID já existe no  vetor
        flag = 1
        while(flag == 1):
            id_produtos[i] = int(input("Insira um ID do valido: "))
            if id_produtos[i] not in id_produtos:
                flag = 0
    nome_produtos.append(input("Insira o nome do produto: "))
    precos_produtos[i] = float(input("Insira o valor do produto: "))
    if (id_produtos[i]%2==0) or (precos_produtos[i]>=1000):
        if (id_produtos[i]%2==0) and (precos_produtos[i]>=1000):
            nome_produtos_att.append(nome_produtos[i])
            id_produtos_att.append(id_produtos[i])
            precos_produtos_att.append(precos_produtos[i]*1.2)
        if (id_produtos[i]%2==0) and (precos_produtos[i]<1000):
            nome_produtos_att.append(nome_produtos[i])
            id_produtos_att.append(id_produtos[i])
            precos_produtos_att.append(precos_produtos[i]*1.15)
        if (id_produtos[i]%2!=0) and (precos_produtos[i]>=1000):
            nome_produtos_att.append(nome_produtos[i])
            id_produtos_att.append(id_produtos[i])
            precos_produtos_att.append(precos_produtos[i]*1.1)


#Print dos produtos com preços atualizados
print("\nProdutos com preço atualizados")
for i in range(len(id_produtos_att)):
    print(f"O Produto {nome_produtos_att[i]} do id {id_produtos_att[i]} está com novo preço de {precos_produtos_att[i]:.2f}")
