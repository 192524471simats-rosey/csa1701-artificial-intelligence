# Water Jug Problem

jug1, jug2 = 4, 3
target = 2

x = y = 0

while x != target:
    if x == 0:
        x = jug1
        print("Fill Jug1:", (x, y))
    elif y == jug2:
        y = 0
        print("Empty Jug2:", (x, y))
    else:
        t = min(x, jug2 - y)
        x -= t
        y += t
        print("Pour Jug1 -> Jug2:", (x, y))

print("Target reached:", (x, y))
