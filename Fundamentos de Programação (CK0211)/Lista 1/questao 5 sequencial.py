#Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
#que este sofreu um desconto de 10%
preco = float(input("Insira o preço do produto: R$"))
novo_preco = preco-(preco*0.1)
print(f"Novo preço é {novo_preco}")