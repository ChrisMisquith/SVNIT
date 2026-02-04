import random

rooms = ['a', 'b', 'c']
loc = 'a'
dir = 'right'

print("percept\t\t\taction\t\tlocation")
print("------------------------------------------------------------")

for step in range(15):

    env = {
        'a': random.choice(['dirt', 'clean']),
        'b': random.choice(['dirt', 'clean']),
        'c': random.choice(['dirt', 'clean'])
    }

    status = env[loc]
    percept = (loc, status)

    if status == 'dirt':
        action = 'suck'
        env[loc] = 'clean'
        print(percept, "\t", action, "\t\t", loc)
        continue

    action = 'move'

    if loc == 'a':
        loc = 'b'

    elif loc == 'c':
        loc = 'b'

    else:
        if dir == 'right':
            loc = 'c'
            dir = 'left'
        else:
            loc = 'a'
            dir = 'right'

    print(percept, "\t", action, "\t\t", loc)