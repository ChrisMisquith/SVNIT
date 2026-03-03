class Node:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent
        self.h = 0  #heuristic cost
        self.f = 0  #f is just h

#manhattan distance (dist = |x1 - x2| + |y1 - y2|)
def get_heuristic(curr_pos, goal_pos):
    return abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])

def greedy_best_first_search(grid, start, goal):
    
    #start node
    start_node = Node(start[0], start[1], None)
    start_node.h = get_heuristic(start, goal)
    start_node.f = start_node.h  #f depends on h

    #open_list is frontier
    #closed_listis tracks visited
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        #node with lowest h score (closest to goal)
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        
        closed_list.append((current_node.row, current_node.col))

        #check goal
        if (current_node.row, current_node.col) == goal:
            path = []
            curr = current_node
            while curr is not None:
                path.append((curr.row, curr.col))
                curr = curr.parent
            return path[::-1]

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)] 

        for offset in neighbors:
            new_row = current_node.row + offset[0]
            new_col = current_node.col + offset[1]

            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[new_row]):
                continue

            if grid[new_row][new_col] == 1:
                continue
            
            if (new_row, new_col) in closed_list:
                continue
            
            new_node = Node(new_row, new_col, current_node)
            
            new_node.h = get_heuristic((new_row, new_col), goal)
            new_node.f = new_node.h 

            #check for neighbor already in open list
            in_open = False
            for open_node in open_list:
                if open_node.row == new_node.row and open_node.col == new_node.col:
                    in_open = True
                    break
            
            if not in_open:
                open_list.append(new_node)

    return None

#main part
grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
]

start_pos = (1, 1)
goal_pos = (5, 11)

print(f"Running Greedy Best-First Search...")

path = greedy_best_first_search(grid, start_pos, goal_pos)

if path:
    print("Path found!")
    print(path)
    
    #visual
    print("\nVisual Map:")
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            if (r, c) == start_pos:
                line += "S "
            elif (r, c) == goal_pos:
                line += "G "
            elif (r, c) in path:
                line += ". "
            elif grid[r][c] == 1:
                line += "# "
            else:
                line += "  "
        print(line)
else:
    print("No path found.")