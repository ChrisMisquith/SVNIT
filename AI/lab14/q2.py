def runb(goal, facts, rules, level):
    print("  " * level + "Goal:", goal)

    if goal in facts:
        print("  " * level + goal + " is fact")
        return True

    for left, right in rules:
        if right == goal:
            print("  " * level + "Try:", " & ".join(left), "->", right)
            ok = True
            for x in left:
                if not runb(x, facts, rules, level + 1):
                    ok = False
                    break
            if ok:
                print("  " * level + goal + " proven")
                return True

    print("  " * level + goal + " fail")
    return False


def case1():
    print("Backward Case 1")
    facts = set(["A", "B"])
    rules = [
        (["P"], "Q"),
        (["R"], "Q"),
        (["A"], "P"),
        (["B"], "R")
    ]
    res = runb("Q", facts, rules, 0)
    print("Result:", "Q derived" if res else "Q not derived")
    print()


def case2():
    print("Backward Case 2")
    facts = set(["A", "E"])
    rules = [
        (["A"], "B"),
        (["B", "C"], "D"),
        (["E"], "C")
    ]
    res = runb("D", facts, rules, 0)
    print("Result:", "D derived" if res else "D not derived")


case1()
case2()