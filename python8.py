# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            dfs(neighbor)

# Driver Code
print("DFS Traversal:", end=" ")
dfs('A')
