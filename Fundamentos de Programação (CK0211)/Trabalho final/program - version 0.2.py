#printa na tela o game
def tela():
    print("\n")
    print("+="*15)
    print("\t  1   2   3 ")
    print(f"\t1 {mat[0][0]} | {mat[0][1]} | {mat[0][2]}  ")
    print("\t ---+---+---")
    print(f"\t2 {mat[1][0]} | {mat[1][1]} | {mat[1][2]}  ")
    print("\t ---+---+---")
    print(f"\t3 {mat[2][0]} | {mat[2][1]} | {mat[2][2]}  ")
    print("+="*15)

#criar a matriz do game
def crie_matriz_game(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)		        # coloque linha na matriz
        matriz.append(linha)	
    return matriz

def pegar_icone():
    print("\nQual icone deseja? ")
    print("1 para 'X'")
    print("2 para 'O'")
    escolha = int(input())
    if escolha == 1:
        player[0] = 'X'
        player[1] = 'O'
    else:
        player[0] = 'O'
        player[1] = 'X'

def regras():
    print("1 - Você vai selecionar o icone do seu jogador, e o complementar ficarar para o computador")
    print("2 - Para realizar a jogada basta inserir as coordenadas desejadas, como padrão temos 'linha,coluna' separado por virgula ")
    print("Divirta-se")


#main
regras()
mat = crie_matriz_game(3,3," ")
player = [0]*2
pegar_icone()
tela()
