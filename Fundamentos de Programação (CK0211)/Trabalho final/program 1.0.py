from random import randint
from time import sleep
#linha necessarias para poder limpar tela
import os

#printa na tela o game
def tela():
    print("\n" * os.get_terminal_size().lines)
    print("\n","+="*15)
    print("\t  1   2   3 ")
    print(f"\t1 {mat[0][0]} | {mat[0][1]} | {mat[0][2]}  ")
    print("\t ---+---+---")
    print(f"\t2 {mat[1][0]} | {mat[1][1]} | {mat[1][2]}  ")
    print("\t ---+---+---")
    print(f"\t3 {mat[2][0]} | {mat[2][1]} | {mat[2][2]}  ")
    print("+="*15)

#criar a matrix do game
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
    cont = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'X' or mat[i][j] == 'O':
                cont+=1
    if cont == 9:
        print("Deu empate Negada")
    else:
        print("Processando jogada da máquina...")
        sleep(4)
        while True:
            linha = randint(0,2)
            coluna = randint(0,2)
            if mat[linha][coluna] not in ('X','O'):
                mat[linha][coluna] = player[1]
                break
            
#Função que reseta toda a matrix
def resetar_game():
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = ' '

#condições de vitoria
def win_conditions():
    for i in range(3):
        print(i)
        if((mat[i][0] ==  mat[i][1]) and (mat[i][1] == mat[i][2]) and (mat[i][0] != " ")):
            if(mat[i][0] == player[0]):
                tela()
                print("\n-------Parabêns, você ganhou!!!!!-------")
                pontuacao[0] += 1
                return 1
            else:
                tela()
                print("\n-------Computador venceu essa!!!!-------")
                pontuacao[1] += 1
                return 1
    for i in range(3):
        if (mat[0][i] ==  mat[1][i] and mat[1][i] == mat[2][i] and mat[1][i] != " "):
            if(mat[1][i] == player[0]):
                tela()
                print("\n-------Parabêns, você ganhou!!!!!-------")
                pontuacao[0] += 1
                return 1
            else:
                tela()
                print("\n-------Computador venceu essa!!!!-------")
                pontuacao[1] += 1
                return 1
    if (mat[0][0] ==  mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0]!= " "):#diagonal principal
        if(mat[0][0] == "X"):
            tela()
            print("\n-------Parabêns, você ganhou!!!!!-------")
            pontuacao[0] += 1
            return 1
        else:
            tela()
            print("\n-------Computador venceu essa!!!!-------")
            pontuacao[1] += 1
            return 1
    if (mat[2][0] ==  mat[1][1] and mat[0][2] ==  mat[1][1] and mat[2][0] != " "):#diagonal segundaria
        if(mat[2][0] == "X"):
            tela()
            print("\n-------Parabêns, você ganhou!!!!!-------")
            pontuacao[0] += 1
            return 1
        else:
            tela()
            print("\n-------Computador venceu essa!!!!-------")
            pontuacao[1] += 1
            return 1
    else:
        return 0
     
def regras():
    sleep(1)
    print("1 - Você vai selecionar o icone do seu jogador, e o complementar ficarar para o computador")
    print("2 - Para realizar a jogada basta inserir as coordenadas desejadas, como padrão temos 'linha,coluna' separado por virgula ")
    print("3 - Atualmente só temos a opção de jogar contra a máquina ")
    print("Divirta-se")
    sleep(5)
    print("\n" * os.get_terminal_size().lines)

#Condição para verificar se o jogo deve finalizar
def processar_ganhador():
    value = win_conditions()
    if value == 1:
        sleep(3)
        return 0
    else:
        return 1

#PRimeira opção do menu
def opcao1():
    flag = 1
    pegar_icone()
    while(flag == 1):
        tela()
        jogada_player()
        flag = processar_ganhador()
        if flag == 0:
            break
        tela()
        jogada_maquina()
        flag = processar_ganhador()
            

def opcao2():
    sleep(1)
    print(f"Jogador {pontuacao[0]} x {pontuacao[1]} Máquina")
    sleep(3)
    print("\n" * os.get_terminal_size().lines)

#Menu do programa
def jogo():
    jogar = 1
    while(jogar == 1):
        print()
        print("=+"*10)
        print(" "*5,"Alb system")
        print("=+"*10)
        print("1 - jogar")
        print("2 - placar")
        print("3 - Regras")
        print("4 - Sair")
        escolha = input()
        while(escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4'):
            print("Valor incorreto, só é aceito 1,2,3 e 4, 'SISTEMA LIMITADO POW!!!!!' ")
            print("1 - jogar")
            print("2 - placar")
            print("3 - Regras")
            print("4 - Sair")
            escolha = input()
        escolha = int(escolha)
        if escolha == 1:
            opcao1()
            resetar_game()
        elif escolha == 2:
            opcao2()
        elif escolha == 3:
            regras()
        elif escolha == 4:
            exit()

#main
mat = crie_matriz_game(3,3," ")
player = [0]*2
pontuacao = [0]*2
jogo()