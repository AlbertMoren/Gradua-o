import random

def print_board(board):
    print("   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  {' | '.join(row)}")
        if i < 2:
            print("  " + "-" * 11)

def check_win(board, player):
    # Check for win in rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def is_move_valid(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def make_move(board, row, col, player):
    if is_move_valid(board, row, col):
        board[row][col] = player
        return True
    else:
        return False

def ai_move(board):
    # Implementation of the Minimax algorithm for the AI
    def minimax(board, depth, maximizing):
        if check_win(board, "O"):
            return 1
        elif check_win(board, "X"):
            return -1
        elif is_board_full(board):
            return 0

        if maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        eval = minimax(board, depth + 1, False)
                        board[i][j] = " "
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        eval = minimax(board, depth + 1, True)
                        board[i][j] = " "
                        min_eval = min(min_eval, eval)
            return min_eval

    # Choose the best move for the AI
    best_value = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = minimax(board, 0, False)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

def tic_tac_toe_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print("\nMenu:")
        print("1. Play")
        print("2. Scoreboard")
        print("3. Rules")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            while not is_board_full(board):
                print_board(board)

                if current_player == "X":
                    row = int(input("Enter the row (0, 1, or 2): "))
                    col = int(input("Enter the column (0, 1, or 2): "))
                    if make_move(board, row, col, current_player):
                        if check_win(board, current_player):
                            print_board(board)
                            print("Congratulations! You won!")
                            break
                        current_player = "O"
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("AI's turn (O)")
                    row, col = ai_move(board)
                    make_move(board, row, col, current_player)
                    if check_win(board, current_player):
                        print_board(board)
                        print("The AI won!")
                        break
                    current_player = "X"

                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break

        elif choice == "2":
            print("Scoreboard: Under construction...")

        elif choice == "3":
            print("\nTic-Tac-Toe Rules:")
            print("1. The game is played on a 3x3 grid.")
            print("2. Each player, X and O, takes turns to make a move on the grid.")
            print("3. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins.")
            print("4. If the grid is full and no player manages to win, the game is a tie.")

        elif choice == "4":
            print("Game closed. See you next time!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tic_tac_toe_game()
