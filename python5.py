from collections import deque

def solve():
    q = deque([((3,3,1), [])])   # (Missionaries, Cannibals, Boat)
    visited = set()

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) == (0,0,0):
            print(path + [(0,0,0)])
            return

        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:
            if b:
                nm, nc, nb = m-dm, c-dc, 0
            else:
                nm, nc, nb = m+dm, c+dc, 1

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and ((3-nm) == 0 or (3-nm) >= (3-nc)):
                    q.append(((nm, nc, nb), path + [(m, c, b)]))

solve()
