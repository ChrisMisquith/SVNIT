from collections import deque

# 0  → Rahul
# 1  → Sneha
# 2  → Neha
# 3  → Arjun
# 4  → Pooja
# 5  → Sunil
# 6  → Maya
# 7  → Akash
# 8  → Aarav
# 9  → Priya
# 10 → Raj

graph = {
    0: [1, 2, 3, 4],   # Rahul → Sneha, Neha, Arjun, Pooja
    1: [5, 6],        # Sneha → Sunil, Maya
    2: [7, 8],        # Neha → Akash, Aarav
    3: [10],          # Arjun → Raj
    4: [9],           # Pooja → Priya
    5: [],            # Sunil
    6: [],            # Maya
    7: [],            # Akash
    8: [],            # Aarav
    9: [],            # Priya
    10: []            # Raj
}

def bfs(start, graph):
    visited = [False] * len(graph)
    q = deque()

    visited[start] = True
    q.append(start)

    print("BFS Traversal:", end=" ")

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nhbr in graph[node]:
            if not visited[nhbr]:
                visited[nhbr] = True
                q.append(nhbr)

    print()

def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=" ")

    for nhbr in graph[node]:
        if not visited[nhbr]:
            dfs(nhbr, graph, visited)


start = 0  #rahul

bfs(start, graph)

visited = [False] * len(graph)
print("DFS Traversal:", end=" ")
dfs(start, graph, visited)

