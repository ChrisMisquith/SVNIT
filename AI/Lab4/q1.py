# City map as adjacency matrix
graph = [
# Chi Det Cle Ind Col Pit Buf Syr NY  Phi Bal Bos Pro Por
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

cities = [
    "chi","det","cle","ind","col","pit","buf",
    "syr","ny","phi","bal","bos","pro","por"
]

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


def expand(node):
    children = []
    s = node.state

    for i in range(len(graph)):
        if graph[s][i] != 0:
            cost = node.path_cost + graph[s][i]
            children.append(Node(i, node, cost))

    return children


def pop_lowest(frontier):
    lowest_index = 0
    for i in range(1, len(frontier)):
        if frontier[i].path_cost < frontier[lowest_index].path_cost:
            lowest_index = i
    return frontier.pop(lowest_index)


def best_first_search(start, goal):
    start_node = Node(start)
    frontier = [start_node]
    reached = {start: start_node}
    paths_explored = 0

    while frontier:
        node = pop_lowest(frontier)
        paths_explored += 1

        if node.state == goal:
            return node, paths_explored

        for child in expand(node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.append(child)

    return None, paths_explored


def get_path(node):
    path = []
    while node:
        path.append(cities[node.state])
        node = node.parent
    return path


start = cities.index("chi")
goal = cities.index("bos")

solution, explored = best_first_search(start, goal)

print("Path:", get_path(solution))
print("Total cost:", solution.path_cost)
print("Number of paths explored:", explored)
