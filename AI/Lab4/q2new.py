# grid representation (9=wall, 1=floor)
grid = [
    [9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,1,1,1,1,1,1,1,1,1,1,1,9],
    [9,1,9,9,9,9,9,9,9,9,9,1,9],
    [9,1,1,1,1,1,1,1,1,1,9,1,9],
    [9,9,9,9,9,9,9,9,9,1,9,1,9],
    [9,1,1,1,1,1,1,9,1,1,1,1,9],
    [9,1,9,9,9,9,1,1,1,9,1,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9]
]

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


def expand(node):
    children = []
    r, c = node.state
    
    # up, down, left, right
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in neighbors:
        nr, nc = r + dr, c + dc
        
        # bounds check
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
            # check if not wall (9)
            if grid[nr][nc] != 9:
                # cost is node cost + grid value (which is 1)
                cost = node.path_cost + grid[nr][nc]
                children.append(Node((nr, nc), node, cost))

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
        path.append(node.state)
        node = node.parent
    return path[::-1] # reversing to show start->goal


start = (1, 1)
goal = (5, 11)

solution, explored = best_first_search(start, goal)

if solution:
    print("Path:", get_path(solution))
    print("Total cost:", solution.path_cost)
    print("Number of paths explored:", explored)
    
    # visualization
    print("\nVisual Map:")
    final_path = get_path(solution)
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            if (r, c) == start:
                line += "S "
            elif (r, c) == goal:
                line += "G "
            elif (r, c) in final_path:
                line += ". "
            elif grid[r][c] == 9:
                line += "# "
            else:
                line += "  "
        print(line)
else:
    print("No path found")