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

#alpha beta
node_count = 0
def alphabeta(b, is_max, alpha, beta):
    global node_count
    node_count += 1

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
                val = alphabeta(b, False, alpha, beta)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = alphabeta(b, True, alpha, beta)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)

                if beta <= alpha:
                    break
        return best

def best_move(b, player):
    if player == "X":
        best_val = -math.inf
        move = -1
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = alphabeta(b, False, -math.inf, math.inf)
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
                val = alphabeta(b, True, -math.inf, math.inf)
                b[i] = " "
                if val < best_val:
                    best_val = val
                    move = i
    return move

#full game
current = "X"

print("game start\n")
print_board(board)

while True:
    move = best_move(board, current)
    board[move] = current

    print(current, "plays at", move)
    print_board(board)

    winner = check_winner(board)

    if winner:
        print("winner:", winner)
        break
    elif is_full(board):
        print("draw")
        break

    current = "O" if current == "X" else "X"

print("nodes explored:", node_count)