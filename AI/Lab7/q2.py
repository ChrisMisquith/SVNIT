import random
import math

def heuristic(board):
    """Number of attacking queen pairs."""
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                attacks += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks


def random_board(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

def first_choice_hill_climbing(board, max_sideways=100):
    """Pick random neighbours until one is better; stop if none found."""
    n = len(board)
    current = list(board)
    initial_h = heuristic(current)
    steps = 0

    while True:
        current_h = heuristic(current)
        if current_h == 0:
            return current, initial_h, 0, steps, True

        improved = False
        attempts = 0

        while attempts < n * (n - 1):       
            col = random.randint(0, n - 1)
            row = random.randint(0, n - 1)
            if row == current[col]:
                continue
            neighbour = list(current)
            neighbour[col] = row
            h = heuristic(neighbour)
            attempts += 1
            if h < current_h:
                current = neighbour
                steps += 1
                improved = True
                break

        if not improved:
            return current, initial_h, heuristic(current), steps, heuristic(current) == 0


def steepest_ascent(board):
    """Basic steepest-ascent (used inside random restart)."""
    n = len(board)
    current = list(board)
    steps = 0

    while True:
        current_h = heuristic(current)
        best_h = current_h
        best_board = list(current)

        for col in range(n):
            orig = current[col]
            for row in range(n):
                if row == orig:
                    continue
                current[col] = row
                h = heuristic(current)
                if h < best_h:
                    best_h = h
                    best_board = list(current)
                current[col] = orig

        if best_h >= current_h:
            return current, current_h, steps
        current = best_board
        steps += 1


def random_restart_hill_climbing(board, max_restarts=50):
    """Restart with a fresh random board whenever steepest-ascent gets stuck."""
    initial_h = heuristic(board)
    total_steps = 0
    restarts = 0

    current = list(board)
    while restarts <= max_restarts:
        final_board, final_h, steps = steepest_ascent(current)
        total_steps += steps
        if final_h == 0:
            return final_board, initial_h, 0, total_steps, True, restarts
        restarts += 1
        current = random_board()

    return final_board, initial_h, final_h, total_steps, False, restarts

def simulated_annealing(board, T0=4.0, cooling=0.995, min_temp=1e-4, max_iter=100000):
    """Classic simulated-annealing schedule for 8-queens."""
    n = len(board)
    current = list(board)
    initial_h = heuristic(current)
    current_h = initial_h
    T = T0
    steps = 0

    for _ in range(max_iter):
        if current_h == 0:
            return current, initial_h, 0, steps, True

        # random neighbour
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        while row == current[col]:
            row = random.randint(0, n - 1)

        neighbour = list(current)
        neighbour[col] = row
        delta = heuristic(neighbour) - current_h

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbour
            current_h = heuristic(current)
            steps += 1

        T *= cooling
        if T < min_temp:
            break

    return current, initial_h, heuristic(current), steps, heuristic(current) == 0

if __name__ == "__main__":
    NUM_BOARDS = 50
    random.seed(42)
    boards = [random_board() for _ in range(NUM_BOARDS)]

    fc_results = []
    rr_results = []
    sa_results = []

    for b in boards:
        fc_results.append(first_choice_hill_climbing(list(b)))
    for b in boards:
        rr_results.append(random_restart_hill_climbing(list(b)))
    for b in boards:
        sa_results.append(simulated_annealing(list(b)))

    fc_solved = sum(1 for r in fc_results if r[4])
    rr_solved = sum(1 for r in rr_results if r[4])
    sa_solved = sum(1 for r in sa_results if r[4])
    fc_avg_steps = sum(r[3] for r in fc_results) / NUM_BOARDS
    rr_avg_steps = sum(r[3] for r in rr_results) / NUM_BOARDS
    sa_avg_steps = sum(r[3] for r in sa_results) / NUM_BOARDS
    rr_avg_restarts = sum(r[5] for r in rr_results) / NUM_BOARDS

    print("--- 8-Queens: Comparative Summary ---")
    print(f"{'Algorithm':<25} {'Solved':<15} {'Avg Steps':<12} {'Avg Restarts'}")
    print("-" * 65)
    print(f"{'First-Choice HC':<25} {fc_solved}/{NUM_BOARDS} ({fc_solved/NUM_BOARDS*100:.0f}%)       {fc_avg_steps:<12.1f} -")
    print(f"{'Random-Restart HC':<25} {rr_solved}/{NUM_BOARDS} ({rr_solved/NUM_BOARDS*100:.0f}%)      {rr_avg_steps:<12.1f} {rr_avg_restarts:.1f}")
    print(f"{'Simulated Annealing':<25} {sa_solved}/{NUM_BOARDS} ({sa_solved/NUM_BOARDS*100:.0f}%)      {sa_avg_steps:<12.1f} -")