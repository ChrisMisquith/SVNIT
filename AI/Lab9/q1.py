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

node_count = 0
total_nodes = 0

def minimax(b, is_max):
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
                val = minimax(b, False)
                b[i] = " "
                best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = minimax(b, True)
                b[i] = " "
                best = min(best, val)
        return best

def show_tree(b, is_max, depth=0, indent=""):
    if depth == 2:
        print(indent + "...")
        return

    winner = check_winner(b)
    if winner:
        print(indent + winner + " win")
        return
    elif is_full(b):
        print(indent + "draw")
        return

    player = "X" if is_max else "O"

    for i in range(9):
        if b[i] == " ":
            b[i] = player
            print(indent + player + " -> " + str(i))
            show_tree(b, not is_max, depth+1, indent + "   ")
            b[i] = " "

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

current = "X"

print("game start\n")
print_board(board)

while True:
    print("search tree for", current)
    show_tree(board, current == "X")

    node_count = 0
    move = best_move(board, current)
    board[move] = current
    total_nodes += node_count

    print(current, "plays", move)
    print("nodes explored:", node_count)
    print_board(board)

    winner = check_winner(board)

    if winner:
        print("winner:", winner)
        break
    elif is_full(board):
        print("draw")
        break

    current = "O" if current == "X" else "X"

print("total nodes explored:", total_nodes)