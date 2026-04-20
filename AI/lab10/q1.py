import math

distance = [
[0, 283, 345, 0, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[283, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, 0, 0, 0],
[345, 0, 0, 144, 0, 189, 133, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 144, 0, 176, 0, 185, 0, 0, 0, 0, 0, 0, 0],
[182, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 256, 189, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 0],
[0, 0, 133, 185, 0, 0, 0, 0, 0, 305, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 150, 0, 0, 248, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 248, 0, 101, 0, 215, 181, 0],
[0, 0, 0, 0, 0, 0, 305, 0, 101, 0, 101, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 215, 0, 0, 0, 50, 107],
[0, 0, 0, 0, 0, 0, 0, 0, 181, 0, 0, 50, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 0]
]

states = {
0: "chicago", 1: "detroit", 2: "cleveland", 3: "columbus", 4: "indianapolis",
5: "buffalo", 6: "pittsburgh", 7: "syracuse", 8: "new york", 9: "philadelphia",
10: "baltimore", 11: "boston", 12: "providence", 13: "portland"
}

start = 0
goal = 11

alphabeta_nodes = 0
print_every = 10


def neighbors(city):
    return [(i, distance[city][i]) for i in range(len(distance)) if distance[city][i] > 0]


def alphabeta(city, visited, bound, depth=0):
    global alphabeta_nodes
    alphabeta_nodes += 1

    if alphabeta_nodes % print_every == 0:
        print(f"[alphabeta] node #{alphabeta_nodes} | depth={depth} | current={states[city]} | bound={bound}")

    if city == goal:
        print(f"[alphabeta] reached goal at {states[city]} | depth={depth}")
        return 0, [city]

    visited.add(city)

    best_cost = float('inf')
    best_path = []

    for nxt, cost in neighbors(city):
        if nxt not in visited:
            val, path = alphabeta(nxt, visited.copy(), best_cost, depth + 1)

            if val != float('inf') and cost + val < best_cost:
                best_cost = cost + val
                best_path = [city] + path

                print(f"[alphabeta] better path: {states[city]} -> {states[nxt]} | cost={best_cost}")

            if best_cost >= bound:
                print(f"[alphabeta] pruned at {states[city]} (best={best_cost} >= bound={bound})")
                break

    return best_cost, best_path


def run():
    best_cost_ab = float('inf')
    best_path_ab = []

    for nxt, cost in neighbors(start):
        print(f"\n[alphabeta] exploring {states[start]} -> {states[nxt]} (cost {cost})")

        val, path = alphabeta(nxt, set(), best_cost_ab, 1)

        if val != float('inf') and cost + val < best_cost_ab:
            best_cost_ab = cost + val
            best_path_ab = [start] + path

            print(f"[alphabeta] new best path via {states[nxt]} | total cost={best_cost_ab}")

    return best_cost_ab, best_path_ab


if __name__ == "__main__":
    ab_cost, ab_path = run()

    print("\nalphabeta path:")
    print(" -> ".join(states[i] for i in ab_path))
    print("cost:", ab_cost)

    print("\nnodes explored:", alphabeta_nodes)