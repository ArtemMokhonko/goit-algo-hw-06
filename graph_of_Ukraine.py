import networkx as nx


# Обласні центри України з координатами
city_positions = {
    "Київ": (30.5234, 50.4501), "Харків": (36.2292, 49.9935), "Одеса": (30.7233, 46.4825),
    "Дніпро": (35.0458, 48.4647), "Львів": (24.0297, 49.8397), "Запоріжжя": (35.1396, 47.8388),
    "Кривий Ріг": (33.3985, 47.9105), "Миколаїв": (31.9946, 46.975), "Маріуполь": (37.5287, 47.0971),
    "Луганськ": (39.317, 48.574), "Вінниця": (28.481, 49.232), "Донецьк": (38.056, 48.044),
    "Севастополь": (33.524, 44.616), "Сімферополь": (34.105, 44.952), "Херсон": (32.6178, 46.6354),
    "Полтава": (34.552, 49.588), "Чернігів": (31.292, 51.505), "Черкаси": (32.061, 49.444),
    "Житомир": (28.658, 50.254), "Суми": (34.804, 50.907), "Хмельницький": (26.981, 49.421),
    "Чернівці": (25.937, 48.291), "Рівне": (26.251, 50.619), "Кропивницький": (32.260, 48.513),
    "Тернопіль": (25.611, 49.553), "Івано-Франківськ": (24.719, 48.923), "Луцьк": (25.332, 50.748),
    "Ужгород": (22.292, 48.622)
}

distances = {
    ("Київ", "Харків"): 477, ("Київ", "Одеса"): 474, ("Київ", "Дніпро"): 477, ("Київ", "Львів"): 540,
    ("Харків", "Дніпро"): 214, ("Одеса", "Миколаїв"): 132, ("Дніпро", "Запоріжжя"): 72,
    ("Львів", "Тернопіль"): 127, ("Львів", "Івано-Франківськ"): 132, ("Запоріжжя", "Маріуполь"): 212,
    ("Миколаїв", "Херсон"): 61, ("Полтава", "Харків"): 144, ("Чернігів", "Київ"): 143,
    ("Черкаси", "Київ"): 192, ("Житомир", "Київ"): 140, ("Суми", "Харків"): 179, 
    ("Хмельницький", "Тернопіль"): 107, ("Чернівці", "Івано-Франківськ"): 133,
    ("Рівне", "Луцьк"): 70, ("Кропивницький", "Дніпро"): 146, ("Тернопіль", "Хмельницький"): 107,
    ("Івано-Франківськ", "Ужгород"): 240, ("Ужгород", "Львів"): 269, ("Харків", "Донецьк"): 267, 
    ("Донецьк","Маріуполь"): 114, ("Донецьк", "Луганськ"): 148, ("Херсон", "Сімферополь"): 265,
    ("Сімферополь", "Севастополь"): 79, ("Житомир", "Вінниця"): 123, ("Житомир", "Рівне"): 160,
    ("Дніпро", "Кривий Ріг"): 130, ("Вінниця", "Чернівці"): 222, ("Одеса", "Вінниця"): 420
}

# Створюємо граф
G = nx.Graph()

# Додаємо вузли з позиціями
for city, pos in city_positions.items():
    G.add_node(city, pos=pos)

# Додаємо ребра з вагами
for (city1, city2), distance in distances.items():
    G.add_edge(city1, city2, weight=distance)