import itertools

letters = ('S','E','N','D','M','O','R','Y')
digits = range(10)

def solve():
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading digit constraint
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND  = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
        MORE  = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
        MONEY = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']

        if SEND + MORE == MONEY:
            return mapping, SEND, MORE, MONEY

solution = solve()

print("="*50)
print("   CRYPTARITHMETIC SOLUTION")
print("="*50)

if solution:
    mapping, SEND, MORE, MONEY = solution
    print("Letter -> Digit Mapping:")

    for k in sorted(mapping):
        print(f"{k} -> {mapping[k]}")

    print("\nValues:")
    print(f"SEND  = {SEND}")
    print(f"MORE  = {MORE}")
    print(f"MONEY = {MONEY}")
else:
    print("No solution found!")