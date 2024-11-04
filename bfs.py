# Practical No. 01
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Set to keep track of visited nodes.

def bfs_recursive(queue, graph, visited):
    if not queue:
        return  # Base case: If the queue is empty, stop the recursion

    # Dequeue the first node in the queue
    node = queue.pop(0)
    print(node, end=" ")  # Process the node

    # Enqueue all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    # Recursive call to continue BFS with the updated queue
    bfs_recursive(queue, graph, visited)

# Driver Code
print("Following is the Breadth-First Search (Recursive):")
start_node = '5'
visited.add(start_node)
bfs_recursive([start_node], graph, visited)  # Initialize with the start node in the queue
