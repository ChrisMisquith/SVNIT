# 0 = false, 1 = true

def agent(train, obs, emg):
    if emg == 1:
        return "gate: lower | hooter: on | train signal: red"
    if obs == 1:
        return "gate: lower | hooter: on | train signal: red"
    if train == 1:
        return "gate: lower | hooter: on | train signal: green"
    return "gate: raise | hooter: off | train signal: green"


cases = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 0, 1),
    (1, 1, 1)
]

print("level crossing simulation\n")

for i, c in enumerate(cases, 1):
    train, obs, emg = c
    print(f"case {i}")
    print(f"percepts -> train:{train}, obstacle:{obs}, emergency:{emg}")
    print("action   ->", agent(train, obs, emg))
    print("_____________________________________________________")
