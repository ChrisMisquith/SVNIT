import random

#distance matrix for 8 cities a-h
DIST = [
    [0,10,15,20,25,30,35,40],   #a
    [12,0,35,15,20,25,30,45],   #b
    [25,30,0,10,40,20,15,35],   #c
    [18,25,12,0,15,30,20,10],   #d
    [22,18,28,20,0,15,25,30],   #e
    [35,22,18,28,12,0,40,20],   #f
    [30,35,22,18,28,32,0,15],   #g
    [40,28,35,22,18,25,12,0],   #h
]

#total number of cities
NUM_CITIES=len(DIST)

#names used when printing tour
CITY_NAMES="ABCDEFGH"


def tour_cost(tour):
    #calculate total distance of the tour
    cost=sum(DIST[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    #add distance to return to start city
    cost+=DIST[tour[-1]][tour[0]]
    return cost


def format_tour(tour):
    #convert numeric tour to city names
    return " -> ".join(CITY_NAMES[c] for c in tour)+" -> "+CITY_NAMES[tour[0]]


#generate random tour
def random_tour():
    t=list(range(NUM_CITIES))
    random.shuffle(t)  #shuffle cities
    return t


def fitness(tour):
    #fitness is inverse of cost
    return 1.0/tour_cost(tour)


def select_parent(population,fitnesses):
    #roulette wheel selection
    total=sum(fitnesses)
    pick=random.uniform(0,total)
    
    cumulative=0
    for ind,f in zip(population,fitnesses):
        cumulative+=f
        
        #select individual when limit reached
        if cumulative>=pick:
            return ind
    
    return population[-1]


def order_crossover_1pt(p1,p2):
    #single point order crossover
    n=len(p1)
    
    #choose crossover point
    cx=random.randint(1,n-1)
    
    #copy first part from parent1
    child=p1[:cx]
    
    #fill remaining cities from parent2
    for gene in p2:
        if gene not in child:
            child.append(gene)
    
    return child


def order_crossover_2pt(p1,p2):
    #two point order crossover
    n=len(p1)
    
    #choose two crossover points
    cx1,cx2=sorted(random.sample(range(1,n),2))
    
    child=[None]*n
    
    #copy middle segment from parent1
    child[cx1:cx2]=p1[cx1:cx2]
    
    #remaining cities from parent2
    fill=[g for g in p2 if g not in child[cx1:cx2]]
    
    idx=0
    for i in range(n):
        if child[i] is None:
            child[i]=fill[idx]
            idx+=1
    
    return child


def mutate(tour,rate=0.1):
    #swap mutation
    if random.random()<rate:
        
        #choose two cities to swap
        i,j=random.sample(range(len(tour)),2)
        tour[i],tour[j]=tour[j],tour[i]
    
    return tour


def genetic_algorithm(crossover_fn,label,pop_size=50,generations=300,mutation_rate=0.15,seed=42):
    #run genetic algorithm for tsp
    
    random.seed(seed)
    
    #create initial population
    population=[random_tour() for _ in range(pop_size)]
    
    #find best tour
    best_tour=min(population,key=tour_cost)
    best_cost=tour_cost(best_tour)
    
    history=[best_cost]

    for gen in range(1,generations+1):
        
        #calculate fitness values
        fitnesses=[fitness(ind) for ind in population]

        new_pop=[]
        
        #elitism keep best solution
        new_pop.append(list(best_tour))

        while len(new_pop)<pop_size:
            
            #select parents
            p1=select_parent(population,fitnesses)
            p2=select_parent(population,fitnesses)
            
            #create child
            child=crossover_fn(p1,p2)
            
            #mutate child
            child=mutate(child,mutation_rate)
            
            new_pop.append(child)

        population=new_pop

        #find best tour in this generation
        gen_best=min(population,key=tour_cost)
        gen_cost=tour_cost(gen_best)

        #update global best
        if gen_cost<best_cost:
            best_cost=gen_cost
            best_tour=list(gen_best)

        history.append(best_cost)

    return best_tour,best_cost,history


#main program
if __name__=="__main__":
    
    print("tsp genetic algorithm 8 cities\n")

    #run ga with 1 point crossover
    tour1,cost1,hist1=genetic_algorithm(order_crossover_1pt,"1pt")

    #run ga with 2 point crossover
    tour2,cost2,hist2=genetic_algorithm(order_crossover_2pt,"2pt")

    #generation where best solution appeared
    first_hit_1=next(i for i,c in enumerate(hist1) if c==cost1)
    first_hit_2=next(i for i,c in enumerate(hist2) if c==cost2)

    print(f"{'crossover':>10} | {'cost':>6} | {'converged':>10} | best tour")
    print("-"*65)

    print(f"{'1 point':>10} | {cost1:>6} | {'gen '+str(first_hit_1):>10} | {format_tour(tour1)}")
    print(f"{'2 point':>10} | {cost2:>6} | {'gen '+str(first_hit_2):>10} | {format_tour(tour2)}")

    print("\ndoes number of crossover points affect convergence")

    if first_hit_2<first_hit_1:
        print("2 point crossover converged faster")
    elif first_hit_1<first_hit_2:
        print("1 point crossover converged faster")
    else:
        print("both converged at same generation")