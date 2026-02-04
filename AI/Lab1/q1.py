from collections import deque

# graph / data
graph = {}

graph["Syracuse"] = {
    "Buffalo": 150,
    "New York": 254,
    "Boston": 312
}

graph["Buffalo"] = {
    "Detroit": 256,
    "Cleveland": 189,
    "Pittsburgh": 215
}

graph["Detroit"] = {
    "Chicago": 283
}

graph["Cleveland"] = {
    "Chicago": 345,
    "Detroit": 169,
    "Columbus": 144
}

graph["Columbus"] = {
    "Indianapolis": 176,
    "Pittsburgh": 185
}

graph["Indianapolis"] = {
    "Chicago": 182
}

graph["Pittsburgh"] = {
    "Philadelphia": 305
}

graph["Philadelphia"] = {
    "New York": 97
}

graph["New York"] = {
    "Boston": 215
}

graph["Boston"] = {}
graph["Chicago"] = {}

#bfs
def bfs_all_paths(start, goal, graph):
    queue = deque([(start, [start], 0)])
    all_paths = []

    while queue:
        node, pth, cst = queue.popleft()

        if node == goal:
            all_paths.append((pth, cst))
            continue

        for nhbr, step_cost in graph[node].items():
            if nhbr not in pth:
                queue.append(
                    (nhbr, pth + [nhbr], cst + step_cost)
                )

    return all_paths

#dfs
def dfs_all_paths(start, goal, graph):
    all_paths = []

    def dfs(node, pth, cst):
        if node == goal:
            all_paths.append((pth, cst))
            return

        for nhbr, step_cost in graph[node].items():
            if nhbr not in pth:
                dfs(nhbr, pth + [nhbr], cst + step_cost)

    dfs(start, [start], 0)
    return all_paths


print("\nBFS - All paths from Syracuse to Chicago:\n")
bfs_paths = bfs_all_paths("Syracuse", "Chicago", graph)
for pth, cst in bfs_paths:
    print(" -> ".join(pth), "| Cost:", cst)

print("\nDFS - All paths from Syracuse to Chicago:\n")
dfs_paths = dfs_all_paths("Syracuse", "Chicago", graph)
for pth, cst in dfs_paths:
    print(" -> ".join(pth), "| Cost:", cst)
