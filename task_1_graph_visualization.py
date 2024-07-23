import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from graph_of_Ukraine import G, city_positions


def visualize_graph():
    # Завантажуємо зображення карти України
    map_img = mpimg.imread('ukraine_map.png')
    
    plt.figure(figsize=(18, 16))
    plt.imshow(map_img, extent=[21, 41, 44, 53], alpha=0.9)
    
    pos = {city: (lon, lat) for city, (lon, lat) in city_positions.items()}
    nx.draw(G, pos, with_labels=True, node_color='yellow', node_size=700, edge_color='skyblue', font_size=8, font_weight='bold', width=2.5)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title('Граф обласних центрів та деяких міст України з вагами (відстанями)')
    plt.xlim(21, 41)
    plt.ylim(44, 53)
    plt.show()

visualize_graph()

# Аналіз характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for city, degree in degrees.items():
    print(f"{city}: {degree}")