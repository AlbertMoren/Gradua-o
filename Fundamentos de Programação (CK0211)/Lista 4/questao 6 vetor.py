'''Faça um programa que receba o total das vendas de cada vendedor de uma loja e armazene-as em um vetor. Receba também o percentual de comissão a que cada vendedor tem direito e armazene-os em outro vetor. Receba os nomes desses vendedores e armazene-os em um terceiro vetor. Existem apenas dez vendedores na loja. Calcule e mostre:
■ um relatório com os nomes dos vendedores e os valores a receber referentes à comissão;
■ o total das vendas de todos os vendedores;
■ o maior valor a receber e o nome de quem o receberá;
■ o menor valor a receber e o nome de quem o receberá.'''
nome_vendedor = []
venda_vendedor = [0]*3
comissao_vendendor = [0]*3
maior = [0]*2
menor = [99999,0]
for i in range(3):
    nome = input("Nome do vendedor: ")
    if nome in nome_vendedor:                           #Valida se o vendedor já se encontra no vetor
        flag = 1
        while(flag == 1):
            nome = input("Vendedor já existe em nosso banco de dados, insira outro: ")
            if nome not in nome_vendedor:
                flag = 0
    nome_vendedor.append(nome)
    venda_vendedor[i] = float(input("Insira o total de venda do vendedor: "))
    comissao_vendendor[i] = float(input("Insira a comissão do vendedor: "))/100
    if venda_vendedor[i] > maior[0]:
        maior[0] = venda_vendedor[i]
        maior[1] = i
    if venda_vendedor[i] < menor[0]:
        menor[0] = venda_vendedor[i]
        menor[1] = i

print("="*5, "RELATÓRIO", "="*5)                        #Imprimi relatório de vendas na tela
for i in range(len(venda_vendedor)):
    print(f"O vendedor {nome_vendedor[i]} fez R${venda_vendedor[i]:.2f}, fica com comissão de R${venda_vendedor[i]*comissao_vendendor[i]:.2f}")
print(f"Houve um total de {sum(venda_vendedor):.2f} vendas")
print(f"O {nome_vendedor[maior[1]]} fez a maior venda, de R${maior[0]:.2f}\nO {nome_vendedor[menor[1]]} fez a maior venda, de R${menor[0]:.2f}")
print("="*20)

