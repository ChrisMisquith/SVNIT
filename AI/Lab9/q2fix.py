distance = [
# chi det cle ind col pit buf syr ny  phi bal bos pro por
[  0,283,345,182,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # chi
[283,  0,169,  0,  0,  0,256,  0,  0,  0,  0,  0,  0,  0], # det
[345,169,  0,  0,144,134,189,  0,  0,  0,  0,  0,  0,  0], # cle
[182,  0,  0,  0,176,  0,  0,  0,  0,  0,  0,  0,  0,  0], # ind
[  0,  0,144,176,  0,185,  0,  0,  0,  0,  0,  0,  0,  0], # col
[  0,  0,134,  0,185,  0,215,  0,  0,305,247,  0,  0,  0], # pit
[  0,256,189,  0,  0,215,  0,150,  0,  0,  0,  0,  0,  0], # buf
[  0,  0,  0,  0,  0,  0,150,  0,254,253,  0,312,  0,  0], # syr
[  0,  0,  0,  0,  0,  0,  0,254,  0, 97,  0,  0,181,  0], # ny
[  0,  0,  0,  0,  0,305,  0,253, 97,  0,101,215,  0,  0], # phi
[  0,  0,  0,  0,  0,247,  0,  0,  0,101,  0,  0,  0,  0], # bal
[  0,  0,  0,  0,  0,  0,  0,312,  0,215,  0,  0, 50,107], # bos
[  0,  0,  0,  0,  0,  0,  0,  0,181,  0,  0, 50,  0,  0], # pro
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,107,  0,  0]  # por
]

states = {
    0: "chicago", 1: "detroit", 2: "cleveland", 3: "columbus", 4: "indianapolis",
    5: "buffalo", 6: "pittsburgh", 7: "syracuse", 8: "new york", 9: "philadelphia",
    10: "baltimore", 11: "boston", 12: "providence", 13: "portland"
}

start = 0
goal = 11

nodes_explored = 0
print_every = 5

best_cost_global = float('inf')
best_path_global = []


def neighbors(city):
    return [(i, distance[city][i]) for i in range(len(distance)) if distance[city][i] > 0]


def alphabeta_style(city, visited, path, cost_so_far, depth=0):
    global nodes_explored, best_cost_global, best_path_global

    nodes_explored += 1

    if nodes_explored % print_every == 0:
        print(f"[search] node #{nodes_explored} | depth={depth} | current={states[city]} | costsofar={cost_so_far} | bestknown={best_cost_global}")

    if cost_so_far >= best_cost_global:
        print(f"[prune] at {states[city]} because costsofar={cost_so_far} >= bestknown={best_cost_global}")
        return

    if city == goal:
        print(f"[goal] reached {states[city]} | total cost={cost_so_far}")
        if cost_so_far < best_cost_global:
            best_cost_global = cost_so_far
            best_path_global = path.copy()
            print(f"[update] new best path = {' -> '.join(states[i] for i in best_path_global)} | cost={best_cost_global}")
        return

    next_nodes = neighbors(city)
    next_nodes.sort(key=lambda x: x[1])

    for nxt, edge_cost in next_nodes:
        if nxt not in visited:
            visited.add(nxt)
            path.append(nxt)

            alphabeta_style(nxt, visited, path, cost_so_far + edge_cost, depth + 1)

            path.pop()
            visited.remove(nxt)


def run():
    global best_cost_global, best_path_global, nodes_explored

    best_cost_global = float('inf')
    best_path_global = []
    nodes_explored = 0

    alphabeta_style(start, {start}, [start], 0, 0)

    return best_cost_global, best_path_global


if __name__ == "__main__":
    final_cost, final_path = run()

    if final_path:
        print("\noptimal path:")
        print(" -> ".join(states[i] for i in final_path))
        print("cost:", final_cost)
    else:
        print("\nno path found")

    print("\nnodes explored:", nodes_explored)