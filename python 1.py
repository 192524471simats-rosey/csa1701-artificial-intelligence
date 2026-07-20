# 8-Puzzle Problem (Simple)

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

print("Initial State:")
for row in start:
    print(row)

print("\nGoal State:")
for row in goal:
    print(row)

print("\nMoves:")
print("Move 5 Up")
print("Move 8 Left")

print("\nPuzzle Solved!")
