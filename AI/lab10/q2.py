# ═══════════════════════════════════════════════════════════════
# State Representation
# ═══════════════════════════════════════════════════════════════

ACTIONS = ['Suck', 'Left', 'Right']


def is_goal(state):
    _, status_a, status_b = state
    return status_a == 'Clean' and status_b == 'Clean'


def erratic_results(state, action):
    loc, status_a, status_b = state
    results = []

    if action == 'Left':
        results.append(('A', status_a, status_b))

    elif action == 'Right':
        results.append(('B', status_a, status_b))

    elif action == 'Suck':
        if loc == 'A':
            if status_a == 'Dirty':
                results.append(('A', 'Clean', status_b))
                results.append(('A', 'Clean', 'Clean'))
            else:
                results.append(('A', 'Clean', status_b))
                results.append(('A', 'Dirty', status_b))
        else:
            if status_b == 'Dirty':
                results.append(('B', status_a, 'Clean'))
                results.append(('B', 'Clean', 'Clean'))
            else:
                results.append(('B', status_a, 'Clean'))
                results.append(('B', status_a, 'Dirty'))

    # remove duplicates
    seen = set()
    unique = []
    for r in results:
        if r not in seen:
            seen.add(r)
            unique.append(r)

    return unique


# ═══════════════════════════════════════════════════════════════
# AND-OR Graph Search
# ═══════════════════════════════════════════════════════════════

def and_or_search(state, path=None):
    if path is None:
        path = []

    if is_goal(state):
        return []

    if state in path:
        return 'failure'

    for action in ACTIONS:
        results = erratic_results(state, action)
        plan = or_search_action(state, action, results, path)

        if plan != 'failure':
            return plan

    return 'failure'


def or_search_action(state, action, results, path):
    conditional_plan = {}

    for result_state in results:
        sub_plan = and_or_search(result_state, path + [state])

        if sub_plan == 'failure':
            return 'failure'

        conditional_plan[result_state] = sub_plan

    if len(results) == 1:
        return [action] + conditional_plan[results[0]]

    return [action, ('if', conditional_plan)]


# ═══════════════════════════════════════════════════════════════
# Display Utilities
# ═══════════════════════════════════════════════════════════════

def format_state(state):
    loc, sa, sb = state
    return f"(Loc={loc}, A={sa}, B={sb})"


def print_plan(plan, indent=0):
    prefix = "  " * indent

    if plan == []:
        print(f"{prefix}[GOAL REACHED]")
        return

    action = plan[0]
    print(f"{prefix}-> {action}")   # FIXED HERE

    if len(plan) == 1:
        return

    step = plan[1]

    if isinstance(step, tuple) and step[0] == 'if':
        conditions = step[1]
        print(f"{prefix}  IF outcomes:")

        for state, sub_plan in conditions.items():
            print(f"{prefix}    Result {format_state(state)}:")
            print_plan(sub_plan, indent + 3)


def print_state_space():
    locations = ['A', 'B']
    statuses = ['Clean', 'Dirty']
    states = []

    for loc in locations:
        for sa in statuses:
            for sb in statuses:
                states.append((loc, sa, sb))

    return states


def print_transition_table(states):
    print(f"\n{'State':<30} {'Action':<8} {'Possible Results'}")
    print("-" * 70)

    for state in states:
        for action in ACTIONS:
            results = erratic_results(state, action)
            results_str = ', '.join(format_state(r) for r in results)
            print(f"{format_state(state):<30} {action:<8} {results_str}")


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    states = print_state_space()

    print("--- Erratic Transition Table ---")
    print_transition_table(states)

    print("\n--- AND-OR Search: Conditional Plans ---")

    test_states = [
        ('A', 'Dirty', 'Dirty'),
        ('B', 'Dirty', 'Dirty'),
        ('A', 'Clean', 'Dirty'),
        ('B', 'Dirty', 'Clean'),
        ('A', 'Clean', 'Clean'),
    ]

    for initial_state in test_states:
        print(f"\nInitial: {format_state(initial_state)}")

        if is_goal(initial_state):
            print("  Already at GOAL.")
            continue

        plan = and_or_search(initial_state)

        if plan == 'failure':
            print("  No plan found.")
        else:
            print("  Plan:")
            print_plan(plan, indent=2)