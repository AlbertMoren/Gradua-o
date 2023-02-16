'''Elabore um programa que preencha uma matriz 12 X 4 com os valores das vendas de uma loja, em que cada linha representa um mês do ano e cada coluna representa uma semana do mês. O programa deverá calcular e mostrar:
■ o total vendido em cada mês do ano, mostrando o nome do mês por extenso;
■ o total vendido em cada semana durante todo o ano;
■ o total vendido pela loja no ano.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

from random import uniform

def crie_matriz(n_linhas, n_colunas, valor):   #Criar matriz desejada
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        
        matriz.append(linha)	
    return matriz

mat = crie_matriz(12,4,0)
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
vendas= []
total = 0 
for i in range(len(mat)):       #Preenchendo a matriz e regra de negocios
    soma = 0
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0,5000)
        soma+=mat[i][j]
    vendas.append(soma)
    total+=soma

print("="*30)                   #Printa relatorio
for i in range(len(vendas)):
    print(f"{mes[i]} | R$ {vendas[i]:.2f}")

print("="*30)
for i in range(len(mat)):       #Printa relatorio 
    soma = 0
    for j in range(len(mat[i])):
        soma+=mat[i][j]
        print(f" {mes[i]} na semana {j+1} foi vendido R$ {soma:.2f}")

print("="*30, f"\nNesse ano foi vendido R${total:.2f}")
