from collections import defaultdict, deque

# Fungsi untuk menambahkan edge ke dalam graf
def add_edge(graph, u, v):
    graph[u].append(v)

# Fungsi BFS untuk mencari jalur terpendek
def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])
    
    if start == end:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == end:
                    return new_path
            
            visited.add(node)

# Inisialisasi graf
graph = defaultdict(list)
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'D')
add_edge(graph, 'B', 'C')
add_edge(graph, 'B', 'E')

start_node = 'A'
end_node = 'C'

shortest_path = bfs_shortest_path(graph, start_node, end_node)
print("Jalur Terpendek (BFS):", shortest_path)
