strt = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

def gen_next(st):
    res = []
    x, y = find_zero(st)
    mv = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in mv:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            tmp = [list(r) for r in st]
            tmp[x][y], tmp[nx][ny] = tmp[nx][ny], tmp[x][y]
            res.append(tuple(tuple(r) for r in tmp))
    return res

def find_zero(st):
    for i in range(3):
        for j in range(3):
            if st[i][j] == 0:
                return i, j

q = [strt]
visited = set()
visited.add(strt)

explr = 0

while q:
    curr = q.pop(0)
    explr += 1

    if curr == goal:
        break

    for nhbr in gen_next(curr):
        if nhbr not in visited:
            visited.add(nhbr)
            q.append(nhbr)

print("States explored before reaching goal:", explr)
