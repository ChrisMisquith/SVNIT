import random


def random_board(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]   # random state


def heuristic(board):
    attacks = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            if board[i] == board[j]:        # row
                attacks += 1

            elif abs(board[i] - board[j]) == abs(i - j):   # diagonal
                attacks += 1

    return attacks                         # h value


def steepest_ascent_hill_climbing(board):

    current = board[:]         # copy
    initial_h = heuristic(current)   # start h
    steps = 0                  # step count

    while True:

        current_h = heuristic(current)   # current h
        best_h = current_h               # best so far
        best_board = current[:]          # best state

        for col in range(len(current)):   # each column

            original_row = current[col]   # save pos

            for row in range(len(current)):   # each row

                if row == original_row:
                    continue

                current[col] = row        # try move
                h = heuristic(current)    # new h

                if h < best_h:            # better?
                    best_h = h
                    best_board = current[:]

                current[col] = original_row   # restore

        if best_h >= current_h:          # local min
            return current, initial_h, current_h, steps, (current_h == 0)

        current = best_board             # move
        steps += 1                       # inc step


if __name__ == "__main__":

    NUM_BOARDS = 50
    random.seed(42)          # fixed seed

    solved_count = 0
    local_min_boards = []

    for i in range(1, NUM_BOARDS + 1):   # 50 boards

        board = random_board()           # new board

        final_board, init_h, final_h, steps, solved = \
            steepest_ascent_hill_climbing(board)

        if solved:
            solved_count += 1
        else:
            local_min_boards.append(
                (i, init_h, final_h, steps, final_board)
            )                            # store fail

    print("\n--- Steepest-Ascent Hill Climbing ---")
    print(f"Solved: {solved_count}/{NUM_BOARDS} "
          f"({solved_count/NUM_BOARDS*100:.1f}%)")
    print(f"Failed: {len(local_min_boards)}/{NUM_BOARDS}")

    if local_min_boards:

        avg_h = sum(b[2] for b in local_min_boards) / len(local_min_boards)
        print(f"Average final h (failures): {avg_h:.2f}")

        example = local_min_boards[0]    # take one

        fb = example[4][:]
        stuck_h = heuristic(fb)          # stuck h

        all_geq = True

        for c in range(len(fb)):
            for r in range(len(fb)):
                if r != fb[c]:
                    neighbour = fb[:c] + [r] + fb[c+1:]
                    if heuristic(neighbour) < stuck_h:
                        all_geq = False   # found better

        print(f"All neighbours h >= {stuck_h}? {all_geq}")  # proof