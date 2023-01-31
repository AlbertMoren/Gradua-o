'''Faça um programa para controlar o estoque de mercadorias de uma empresa. Inicialmente, o programa deverá preencher dois vetores com dez posições cada, onde o primeiro corresponde ao código do produto e o
segundo, ao total desse produto em estoque. Logo após, o programa deverá ler um conjunto indeterminado
de dados contendo o código de um cliente e o código do produto que ele deseja comprar, juntamente com a
quantidade. Código do cliente igual a zero indica fim do programa. O programa deverá verificar:
■ se o código do produto solicitado existe. Se existir, tentar atender ao pedido; caso contrário, exibir
mensagem Código inexistente;
■ cada pedido feito por um cliente só pode ser atendido integralmente. Caso isso não seja possível,
escrever a mensagem Não temos estoque suficiente dessa mercadoria. Se puder atendê-lo, escrever
a mensagem Pedido atendido. Obrigado e volte sempre;
■ efetuar a atualização do estoque somente se o pedido for atendido integralmente;
■ no final do programa, escrever os códigos dos produtos com seus respectivos estoques já atualizados.'''
codigo = []
qtd = []
for i in range(3):
    cod,qt = input("Codigo e quantidade do produto: ").split(" ")
    cod = int(cod)
    qt = int(qt)
    codigo.append(cod)
    qtd.append(qt)
cliente = 1
while(cliente != 0):
    cliente = int(input("Código cliente: "))
    if(cliente == 0):
        break
    desejada = int(input("Codigo do produto desejada: "))
    if desejada not in codigo:                                          #trecho responsável por validar a entrada do usúario
        flag = 1
        while(flag == 1):
            print("Produto não existe, insira um válido")
            desejada = int(input("Codigo do produto desejada: "))
            if desejada in codigo:
                flag = 0                                                #vai até aqui
    qt_desejada = int(input("Qual a quantidade desejada? "))             #Trecho respónsavel por achar o produto e interar o valor dele
    for i in range(len(codigo)):
        if(desejada == codigo[i]):
            if(qtd[i] < qt_desejada):
                print("Não temos estoque suficiente dessa mercadoria")
            else:
                qtd[i] = qtd[i] - qt_desejada
                print("Pedido atendido. Obrigado e volte sempre")
for i in range(3):
    print(f"Codigo {codigo[i]} | quantidade {qtd[i]}")

    