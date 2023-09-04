from collections import defaultdict, deque

# Fungsi untuk menambahkan edge ke dalam graf
def add_edge(graph, u, v):
    graph[u].append(v)

# Fungsi DFS untuk mencari jalur terpendek
def dfs_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    
    if start == end:
        return path
    
    shortest_path = None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_shortest_path(graph, neighbor, end, path)
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    
    return shortest_path

# Inisialisasi graf
graph = defaultdict(list)
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'D')
add_edge(graph, 'B', 'C')
add_edge(graph, 'B', 'E')

start_node = 'A'
end_node = 'C'

shortest_path = dfs_shortest_path(graph, start_node, end_node)
print("Jalur Terpendek (DFS):", shortest_path)
