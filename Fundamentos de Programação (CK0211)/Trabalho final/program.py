#printa na tela o game
def tela():
    print("  1   2   3 ")
    print("1   |   |   ")
    print(" ---+---+---")
    print("2   |   |   ")
    print(" ---+---+---")
    print("3   |   |   ")

#criar a matriz do game
def crie_matriz_game(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        # coloque linha na matriz
        matriz.append(linha)	
    return matriz


#main
tela()
mat = crie_matriz_game(3,3,0)