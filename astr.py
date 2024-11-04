# A* Algorithm Implementation
def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Initialize open set with the start node
    closed_set = set()            # Closed set to track visited nodes
    g = {}                         # Distance from start node
    parents = {}                   # Track parent nodes for path reconstruction

    g[start_node] = 0              # Distance of start node from itself is 0
    parents[start_node] = start_node  # Start node is its own parent

    while open_set:
        n = None
        # Find the node with the lowest f() = g() + h() value
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node:
            # Reconstruct path from stop_node to start_node
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # Check neighbors of current node n
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                # Update g(m) if a shorter path is found
                g[m] = g[n] + weight
                parents[m] = n
                # Move m from closed set to open set if necessary
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)

        # Move n from open set to closed set after checking all neighbors
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Function to get neighbors and their distances
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Heuristic function for A*
def heuristic(n):
    H_dict = {
        'S': 14,
        'B': 12,
        'C': 11,
        'D': 6,
        'E': 4,
        'F': 11,
        'G': 0
    }
    return H_dict[n]

# Define graph with nodes and edges
Graph_nodes = {
  'S': [('B', 4), ('C', 3)],
  'B': [('F', 5), ('E', 12)],
  'C': [('D', 7),  ('E', 10)],
  'D': [('E', 2)],
  'E': [('G', 5)],
  'F': [('G', 16)],
  'G': [],
}

# Execute A* algorithm
aStarAlgo('S', 'G')
