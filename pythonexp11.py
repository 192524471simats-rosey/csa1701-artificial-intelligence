# Map Coloring using CSP

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

# Check if color can be assigned
def safe(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

# Backtracking function
def solve(nodes):
    if not nodes:
        return True

    node = nodes[0]

    for color in colors:
        if safe(node, color):
            result[node] = color
            if solve(nodes[1:]):
                return True
            del result[node]

    return False

# Run the program
if solve(list(graph.keys())):
    print("Solution:")
    for node in result:
        print(node, "->", result[node])
else:
    print("No solution found")
