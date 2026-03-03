total_girls = 3
total_booys = 3

initial_state = (3, 3, 0)
goal_state = (0, 0, 1)

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]


def is_valid(state):
    g_left, b_left, boat = state

    g_right = total_girls - g_left
    b_right = total_booys - b_left

    if g_left < 0 or b_left < 0 or g_right < 0 or b_right < 0:
        return False

    if g_left > 0 and b_left > g_left:
        return False

    if g_right > 0 and b_right > g_right:
        return False

    return True


def generate_next(state):
    g, b, boat = state
    next_states = []

    for mg, mb in moves:
        if boat == 0:
            new_state = (g - mg, b - mb, 1)
        else:
            new_state = (g + mg, b + mb, 0)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


#depth limited search
def dls(state, depth, limit, path, reached, counter):
    counter[0] += 1

    if state == goal_state:
        return path

    if depth == limit:
        return None

    reached.add(state)

    for next_state in generate_next(state):
        if next_state not in reached:
            result = dls(next_state, depth + 1, limit,
                         path + [next_state], reached, counter)
            if result:
                return result

    reached.remove(state)
    return None


#iterative deepening search
def ids():
    depth = 0
    total_explored = 0

    while True:
        reached = set()
        counter = [0]

        result = dls(initial_state, 0, depth,
                     [initial_state], reached, counter)

        total_explored += counter[0]

        if result:
            return result, total_explored

        depth += 1


print("depth limited search limit = 5")

reached = set()
counter = [0]

result = dls(initial_state, 0, 5,
             [initial_state], reached, counter)

if result:
    print("solution found")
    for step in result:
        print(step)
else:
    print("no solution within depth 3")

print("states explored:", counter[0])


print("\niterative deepening search")

solution, explored = ids()

print("solution found")
for step in solution:
    print(step)

print("total states explored:", explored)
