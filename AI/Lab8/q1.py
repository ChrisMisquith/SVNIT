import random

#distance matrix for 8 cities a-h
distance_matrix = [
    [0, 10, 15, 20, 25, 30, 35, 40],
    [12, 0, 35, 15, 20, 25, 30, 45],
    [25, 30, 0, 10, 40, 20, 15, 35],
    [18, 25, 12, 0, 15, 30, 20, 10],
    [22, 18, 28, 20, 0, 15, 25, 30],
    [35, 22, 18, 28, 12, 0, 40, 20],
    [30, 35, 22, 18, 28, 32, 0, 15],
    [40, 28, 35, 22, 18, 25, 12, 0]
]

#list of city indexes
cities = list(range(len(distance_matrix)))

#city names for printing
city_labels = "ABCDEFGH"


def calculate_cost(route):
    #calculate total tour distance
    total = 0

    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]

    #add cost to return to start
    total += distance_matrix[route[-1]][route[0]]

    return total


def generate_random_route():
    #create random tour
    route = list(cities)
    random.shuffle(route)
    return route


def generate_neighbours(route):
    #create neighbours by swapping two cities
    neighbour_list = []

    n = len(route)

    for i in range(n):
        for j in range(i + 1, n):

            new_route = route.copy()

            new_route[i], new_route[j] = new_route[j], new_route[i]

            neighbour_list.append(new_route)

    return neighbour_list


#local beam search algorithm
def beam_search(k, max_iterations=500, seed=10):

    random.seed(seed)

    #generate k random solutions
    beam_states = [generate_random_route() for _ in range(k)]

    best_solution = min(beam_states, key=calculate_cost)

    best_cost = calculate_cost(best_solution)

    history = [best_cost]

    for iteration in range(1, max_iterations + 1):

        all_candidates = []

        #generate neighbours for each beam state
        for state in beam_states:

            neighbours = generate_neighbours(state)

            all_candidates.extend(neighbours)

        #sort neighbours by cost
        all_candidates.sort(key=calculate_cost)

        #keep best k solutions
        beam_states = all_candidates[:k]

        current_best = beam_states[0]

        current_cost = calculate_cost(current_best)

        #update best solution
        if current_cost < best_cost:

            best_cost = current_cost

            best_solution = current_best.copy()

        history.append(best_cost)

        #stop if no improvement for many iterations
        if len(history) > 20 and history[-1] == history[-21]:

            break

    return best_solution, best_cost, history, iteration


def print_tour(route):
    #convert route numbers to city letters
    return " -> ".join(city_labels[i] for i in route) + " -> " + city_labels[route[0]]


#run algorithm for different beam widths
if __name__ == "__main__":

    print("travelling salesman problem using local beam search\n")

    print(f"{'k':>4} | {'cost':>6} | {'iter':>5} | best tour")

    print("-" * 55)

    results = {}

    for k in [3, 5, 10]:

        route, cost, history, iterations = beam_search(k)

        results[k] = (route, cost, history, iterations)

        print(f"{k:>4} | {cost:>6} | {iterations:>5} | {print_tour(route)}")

    print("\ndoes convergence depend on k?")

    costs = {k: results[k][1] for k in results}

    if costs[3] == costs[5] == costs[10]:

        print("all beam widths reached the same cost")

        print("for small problems even small k works")

    else:

        print("larger beam width explores more states")

        print("and may find better solutions")