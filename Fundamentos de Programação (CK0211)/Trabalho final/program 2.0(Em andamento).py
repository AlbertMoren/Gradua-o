from random import randint
from time import sleep

#printa na tela o game
def tela():
    print("\n","+="*15)
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

#Usuario seleciona seu icone e valida se é uma opção valida
def pegar_icone():
    print("\nQual icone deseja? ")
    print("1 para 'X'")
    print("2 para 'O'")
    escolha = input()
    while(escolha != '1' and escolha != '2'):
        print("Valor incorreto, só é aceito 1 e 2")
        print("1 para 'X'")
        print("2 para 'O'")
        escolha = input()
    escolha = int(escolha)
    if escolha == 1:
        player[0] = 'X'
        player[1] = 'O'
    else:
        player[0] = 'O'
        player[1] = 'X'
    sleep(3)
    print(f" ** Você sera o '{player[0]}' e a máquina será '{player[1]}' **")
      
#Função que solicita a jogada do player e a valida
def jogada_player():
    linha = 0
    coluna = 0
    linha,coluna = input("Informe a sua jogada: ").split(",")
    linha = int(linha)
    coluna = int(coluna)
    print("Processando sua jogada...")
    sleep(2)
    flag = 1
    while(flag == 1):
        if linha-1>2 or linha-1<0 or coluna-1>2 or coluna-1<0 or mat[linha-1][coluna-1] == "X" or mat[linha-1][coluna-1] == "O":
            print("Jogada invalida, tente novamente")
            linha,coluna = input("Informe a sua jogada: ").split(",")
            linha = int(linha)
            coluna = int(coluna)
            print("Processando sua jogada...")
            sleep(2)
        else:
            mat[linha-1][coluna-1] = player[0]
            flag = 0
    
#Função que execulta a jogada da maquina e a valida
def jogada_maquina():
    print("Processando jogada da máquina...")
    sleep(4)
    linha = randint(0,3)
    coluna = randint(0,3)
    flag = 1
    while(flag == 1):
        if linha>2 or linha<0 or coluna>2 or coluna<0 or mat[linha][coluna] == "X" or mat[linha][coluna] == "O":
            linha = randint(0,3)
            coluna = randint(0,3)
        else:
            mat[linha][coluna] = player[1]
            flag = 0

#condições de vitoria
def win_conditions():
    if (mat[0][0] == "X" and mat[0][1] == "X" and mat[0][2] == "X") or (mat[0][0] == "O" and mat[0][1] == "O" and mat[0][2] == "O"):
        if(mat[0][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[1][0] == "X" and mat[1][1] == "X" and mat[1][2] == "X") or (mat[1][0] == "O" and mat[1][1] == "O" and mat[1][2] == "O"):
        if(mat[1][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[2][0] == "X" and mat[2][1] == "X" and mat[2][2] == "X") or (mat[2][0] == "O" and mat[2][1] == "O" and mat[2][2] == "O"):
        if(mat[2][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[0][0] == "X" and mat[1][0] == "X" and mat[2][0] == "X") or (mat[0][0] == "O" and mat[1][0] == "O" and mat[2][0] == "O"):
        if(mat[0][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[0][1] == "X" and mat[1][1] == "X" and mat[2][1] == "X") or (mat[0][1] == "O" and mat[1][1] == "O" and mat[2][1] == "O"):
        if(mat[0][1] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[0][2] == "X" and mat[1][2] == "X" and mat[2][2] == "X") or (mat[0][2] == "O" and mat[1][2] == "O" and mat[2][2] == "O"):
        if(mat[0][2] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[0][0] == "X" and mat[1][1] == "X" and mat[2][2] == "X") or (mat[0][0] == "O" and mat[1][1] == "O" and mat[2][2] == "O"):
        if(mat[0][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    elif (mat[2][0] == "X" and mat[1][1] == "X" and mat[0][2] == "X") or (mat[2][0] == "O" and mat[1][1] == "O" and mat[0][2] == "O"):
        if(mat[2][0] == "X"):
            print("\n-------Parabêns, você ganhou!!!!!-------")
            return 1
        else:
            print("\n-------Computador venceu essa!!!!-------")
            return 1
    else:
        return 0
     
def regras():
    print("1 - Você vai selecionar o icone do seu jogador, e o complementar ficarar para o computador")
    print("2 - Para realizar a jogada basta inserir as coordenadas desejadas, como padrão temos 'linha,coluna' separado por virgula ")
    print("3 - Atualmente só temos a opção de jogar contra a máquina ")
    print("Divirta-se")

#Condição para verificar se o jogo deve finalizar
def processar_ganhador():
    value = win_conditions()
    if value == 1:
        tela()
        exit()

#main
regras()
mat = crie_matriz_game(3,3," ")
player = [0]*2
pegar_icone()
flag = 1
while(flag == 1):
    tela()
    jogada_player()
    processar_ganhador()
    tela()
    jogada_maquina()
    processar_ganhador()
    