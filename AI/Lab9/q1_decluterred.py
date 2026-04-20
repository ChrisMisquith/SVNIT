import math

board = [" " for _ in range(9)]

def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for x,y,z in wins:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]
    return None

def is_full(b):
    return " " not in b

def minimax(b, is_max):
    winner = check_winner(b)

    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif is_full(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

def best_move(b, player):
    if player == "X":
        best_val = -math.inf
        move = -1
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = minimax(b, False)
                b[i] = " "
                if val > best_val:
                    best_val = val
                    move = i
    else:
        best_val = math.inf
        move = -1
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = minimax(b, True)
                b[i] = " "
                if val < best_val:
                    best_val = val
                    move = i
    return move

#full game loop
current = "X"

print("Game Start:\n")
print_board(board)

while True:
    move = best_move(board, current)
    board[move] = current

    print(f"{current} plays at position {move}")
    print_board(board)

    winner = check_winner(board)
    if winner:
        print("Winner:", winner)
        break
    elif is_full(board):
        print("Game Draw")
        break

    current = "O" if current == "X" else "X"