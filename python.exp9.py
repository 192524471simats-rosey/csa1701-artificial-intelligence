from itertools import permutations

n = int(input("Enter number of cities: "))

cost = []
print("Enter the cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

min_cost = 99999

for path in permutations(range(1, n)):
    total = 0
    k = 0

    for city in path:
        total += cost[k][city]
        k = city

    total += cost[k][0]

    if total < min_cost:
        min_cost = total

print("Minimum Cost =", min_cost)
