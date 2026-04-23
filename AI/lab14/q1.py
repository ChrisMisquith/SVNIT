def runf(facts, rules, goal, name):
    print(name)
    print("Start:", facts)
    step = 1

    changed = True
    while changed:
        changed = False
        for left, right in rules:
            ok = True
            for x in left:
                if x not in facts:
                    ok = False
                    break
            if ok and right not in facts:
                print("Step", step, ":", " & ".join(left), "->", right)
                facts.add(right)
                print("Now:", facts)
                step += 1
                changed = True

    print("Result:", goal, "derived" if goal in facts else "not derived")
    print()


f1 = set(["A", "B", "M"])
r1 = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]

f2 = set(["A", "E"])
r2 = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]

runf(f1, r1, "Q", "Forward Case 1")
runf(f2, r2, "F", "Forward Case 2")