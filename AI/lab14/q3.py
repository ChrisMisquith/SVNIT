def neg(x):
    return x[1:] if x.startswith("~") else "~" + x


def resolve(c1, c2):
    res = []
    for a in c1:
        for b in c2:
            if a == neg(b):
                new = set(c1 + c2)
                new.discard(a)
                new.discard(b)
                res.append(list(new))
    return res


def run(clauses, goal, name):
    print(name)
    clauses = [list(c) for c in clauses]
    clauses.append([neg(goal)])
    print("Clauses:", clauses)

    step = 1
    while True:
        new = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                res = resolve(clauses[i], clauses[j])
                for r in res:
                    print("Step", step, ":", clauses[i], "+", clauses[j], "=>", r)
                    step += 1
                    if r == []:
                        print("Empty clause found")
                        print("Result:", goal, "derived")
                        print()
                        return
                    if r not in clauses and r not in new:
                        new.append(r)
        if not new:
            print("No contradiction")
            print("Result:", goal, "not derived")
            print()
            return
        clauses += new


c1 = [
    ["P", "Q"],
    ["~P", "R"],
    ["~Q", "S"],
    ["~R", "S"]
]

c2 = [
    ["~P", "Q"],
    ["~Q", "R"],
    ["~S", "~R"],
    ["P"]
]

run(c1, "S", "Resolution Case 1")
run(c2, "S", "Resolution Case 2")