import heapq

# Fungsi untuk menambahkan edge ke dalam graf
def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))
    
# Fungsi Dijkstra untuk mencari jalur terpendek
def dijkstra(graph, start, end):
    # Inisialisasi jarak ke semua simpul dengan nilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Inisialisasi priority queue dengan simpul awal dan jarak nol
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil simpul dengan jarak terpendek saat ini dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika kita telah mencapai simpul tujuan, selesai
        if current_node == end:
            break
        
        # Skip simpul yang sudah dikunjungi sebelumnya
        if current_distance > distances[current_node]:
            continue
        
        # Iterasi melalui tetangga-tetangga dari simpul saat ini
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Jika jarak baru lebih pendek dari jarak yang sudah ada, perbarui jarak
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Jalur terpendek
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        for neighbor, weight in graph[current]:
            if distances[current] == distances[neighbor] + weight:
                current = neighbor
                break
    path.insert(0, start)
    
    return path

# Inisialisasi graf berbobot
graph = {
    'A': [('B', 2), ('D', 1)],
    'B': [('A', 2), ('C', 3), ('E', 1)],
    'C': [('B', 3), ('F', 4)],
    'D': [('A', 1), ('E', 4)],
    'E': [('B', 1), ('D', 4), ('F', 4)],
    'F': [('C', 4), ('E', 4)]
}

start_node = 'A'
end_node = 'F'

shortest_path = dijkstra(graph, start_node, end_node)
print("Jalur Terpendek (Dijkstra):", shortest_path)
