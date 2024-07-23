from graph_of_Ukraine import G
from collections import deque

# Ітеративний алгоритм BFS
def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)
    return order

# Рекурсивний алгоритм DFS
def dfs_recursive(graph, vertex, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(vertex)
    order.append(vertex)  # Відвідуємо вершину
    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)
    return order

# Функція для виводу результатів обходу
def print_results(func, graph, start, algorithm_name):
    print(f"{algorithm_name} обхід:")
    order = func(graph, start)
    print(" -> ".join(order))
    

start_city = "Київ"

print_results(bfs_iterative, G, start_city, "BFS")
print_results(dfs_recursive, G, start_city, "DFS")

