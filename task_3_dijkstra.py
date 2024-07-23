from graph_of_Ukraine import G, city_positions


# Функція для алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)
    previous_nodes = {vertex: None for vertex in graph.nodes}
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor]['weight']
            new_distance = distances[current_vertex] + edge_weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex
        
        unvisited.remove(current_vertex)
    
    return distances, previous_nodes

start_city = "Київ"

# Виконання алгоритму Дейкстри
distances, previous_nodes = dijkstra(G, start_city)
    
    # Вивід результатів алгоритму Дейкстри
print("\nРезультати алгоритму Дейкстри:")
for city, distance in distances.items():
    print(f"Відстань від {start_city} до {city}: {distance} км")