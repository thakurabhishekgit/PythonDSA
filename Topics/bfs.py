from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add neighbors to the queue
            queue.extend(graph[node])
    
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add neighbors to the stack
            stack.extend(graph[node])
    
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal:", bfs(graph, 'A'))
print("DFS Traversal (Iterative):", dfs_iterative(graph, 'A'))