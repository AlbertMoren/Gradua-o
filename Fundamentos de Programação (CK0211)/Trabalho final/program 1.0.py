from random import randint
from time import sleep
import os

def tela():
    print("\n" * os.get_terminal_size().lines)
    print("\n", "+=" * 15)
    print("\t  1   2   3 ")
    print(f"\t1 {mat[0][0]} | {mat[0][1]} | {mat[0][2]}  ")
    print("\t ---+---+---")
    print(f"\t2 {mat[1][0]} | {mat[1][1]} | {mat[1][2]}  ")
    print("\t ---+---+---")
    print(f"\t3 {mat[2][0]} | {mat[2][1]} | {mat[2][2]}  ")
    print("+=" * 15)

def crie_matriz_game(n_linhas, n_colunas, valor):
    matriz = [[valor] * n_colunas for _ in range(n_linhas)]
    return matriz

def pegar_icone():
    print("\nQual ícone deseja? ")
    print("1 para 'X'")
    print("2 para 'O'")
    
    while True:
        escolha = input()
        if escolha in ('1', '2'):
            global player
            player = ('X', 'O') if escolha == '1' else ('O', 'X')
            break
        print("Valor incorreto, só é aceito 1 e 2")

    sleep(3)
    print(f" ** Você será o '{player[0]}' e a máquina será '{player[1]}' **")

def jogada_player():
    while True:
        try:
            linha, coluna = map(int, input("Informe a sua jogada (linha,coluna): ").split(","))
        except ValueError:
            print("Entrada inválida. Use o formato linha,coluna.")
            continue

        print("Processando sua jogada...")
        sleep(2)

        if 1 <= linha <= 3 and 1 <= coluna <= 3 and mat[linha-1][coluna-1] == " ":
            mat[linha-1][coluna-1] = player[0]
            break
        else:
            print("Jogada inválida, tente novamente")

def jogada_maquina():
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if mat[i][j] == ' ':
                mat[i][j] = player[1]
                score = minimax(mat, 0, False)
                mat[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    mat[best_move[0]][best_move[1]] = player[1]

def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'Tie': 0}

    result = win_conditions()
    if result in scores:
        return scores[result]

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player[1]
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player[0]
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score        

def resetar_game():
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = ' '

def win_conditions():
    for i in range(3):
        if all(cell == mat[i][0] and cell != " " for cell in mat[i]):
            return mat[i][0]

        if all(cell == mat[0][i] and cell != " " for cell in [mat[j][i] for j in range(3)]):
            return mat[0][i]

    if mat[0][0] == mat[1][1] == mat[2][2] and mat[0][0] != " ":
        return mat[0][0]

    if mat[2][0] == mat[1][1] == mat[0][2] and mat[2][0] != " ":
        return mat[2][0]

    return None

def regras():
    sleep(1)
    print("1 - Você vai selecionar o ícone do seu jogador, e o complementar ficará para o computador")
    print("2 - Para realizar a jogada basta inserir as coordenadas desejadas, como padrão temos 'linha,coluna' separado por vírgula ")
    print("3 - Atualmente só temos a opção de jogar contra a máquina ")
    print("Divirta-se")
    sleep(5)
    print("\n" * os.get_terminal_size().lines)

def opcao1():
    flag = 1
    pegar_icone()
    while flag:
        tela()
        jogada_player()
        vencedor = win_conditions()
        if vencedor:
            tela()
            print(f"\n-------Parabéns, {vencedor} ganhou!!!!!-------")
            pontuacao[0 if vencedor == player[0] else 1] += 1
            break

        tela()
        jogada_maquina()
        vencedor = win_conditions()
        if vencedor:
            tela()
            print(f"\n-------Computador venceu essa!!!!-------")
            pontuacao[1] += 1
            break

def opcao2():
    sleep(1)
    print(f"Jogador {pontuacao[0]} x {pontuacao[1]} Máquina")
    sleep(3)
    print("\n" * os.get_terminal_size().lines)

def jogo():
    jogar = 1
    while jogar == 1:
        print()
        print("=+" * 10)
        print(" " * 5, "Alb system")
        print("=+" * 10)
        print("1 - jogar")
        print("2 - placar")
        print("3 - Regras")
        print("4 - Sair")
        escolha = input()
        while escolha not in ('1', '2', '3', '4'):
            print("Valor incorreto, só é aceito 1, 2, 3 e 4, 'SISTEMA LIMITADO POW!!!!!' ")
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

mat = crie_matriz_game(3, 3, " ")
player = [0] * 2
pontuacao = [0] * 2
jogo()
