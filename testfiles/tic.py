# Tic Tac Toe Game

board = [" "]*9

def show():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

def check_win(s):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,1,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==s for a,b,c in wins)

turn = "X"

for i in range(9):
    show()
    print(f"Player {turn}'s turn")
    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] != " ":
        print("Invalid move! Try again.")
        continue

    board[pos] = turn

    if check_win(turn):
        show()
        print("Player", turn, "wins!")
        break

    turn = "O" if turn == "X" else "X"
else:
    show()
    print("It's a draw!")
