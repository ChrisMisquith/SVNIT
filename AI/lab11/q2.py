digits = [0] * 10
solution_found = False
m = 1
o = 0
digits[m] = 1  # digit 1 is used by m
digits[o] = 1  # digit 0 is used by o

for s in range(1, 10):
    if digits[s]: continue
    digits[s] = 1
    for e in range(10):
        if digits[e]: continue
        digits[e] = 1
        for n in range(10):
            if digits[n]: continue
            digits[n] = 1
            for d in range(10):
                if digits[d]: continue
                digits[d] = 1
                for r in range(10):
                    if digits[r]: continue
                    digits[r] = 1

                    # Compute y and carry from d + e
                    total = d + e
                    y = total % 10
                    c1 = total // 10

                    if digits[y]: 
                        digits[r] = 0
                        continue

                    # Check n + r + c1 = e + 10*c2
                    nr = n + r + c1
                    if (nr % 10) != e:
                        digits[r] = 0
                        continue
                    c2 = nr // 10

                    # Check e + o + c2 = n + 10*c3
                    eo = e + o + c2
                    if (eo % 10) != n:
                        digits[r] = 0
                        continue
                    c3 = eo // 10

                    # Check s + m + c3 = o + 10 (final carry must give m=1)
                    sm = s + m + c3
                    if sm % 10 != o or sm // 10 != m:
                        digits[r] = 0
                        continue

                    digits[y] = 1
                    send  = s*1000 + e*100 + n*10 + d
                    more  = m*1000 + o*100  + r*10 + e
                    money = m*10000 + o*1000 + n*100 + e*10 + y

                    if send + more == money:
                        print("Solution found!")
                        print(f"s={s} e={e} n={n} d={d} m={m} o={o} r={r} y={y}")
                        print(f"  {send}\n+ {more}\n= {money}")
                        solution_found = True

                    digits[y] = 0
                    digits[r] = 0
                    if solution_found: break
                if solution_found: break
                digits[d] = 0
            if solution_found: break
            digits[n] = 0
        if solution_found: break
        digits[e] = 0
    if solution_found: break
    digits[s] = 0

if not solution_found:
    print("No solution found")