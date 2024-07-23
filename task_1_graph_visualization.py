import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from graph_of_Ukraine import G, city_positions


# Завантажуємо зображення карти України
map_img = mpimg.imread('ukraine_map.png')  

# Візуалізуємо граф
plt.figure(figsize=(18, 16))

# Відображаємо зображення на фоні
plt.imshow(map_img, extent=[21, 41, 44, 53], alpha=0.5)

# Конвертуємо позиції в формат, який зрозуміє networkx
pos = {city: (lon, lat) for city, (lon, lat) in city_positions.items()}

# Відображаємо граф на фоні карти
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='yellow', font_size=10, font_weight='bold', width=1.5)
plt.title('Граф обласних центрів України')
plt.xlim(21, 41)
plt.ylim(44, 53)
plt.show()

# Аналіз характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for city, degree in degrees.items():
    print(f"{city}: {degree}")
