"""
Завдання 3: Вивід найкоротших шляхів з заданої верешини
"""

import networkx as nx
from prettytable import PrettyTable


def print_shortest_paths_from_node(G, start_node):
    shortest_paths = nx.single_source_dijkstra_path(G, source=start_node)
    shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=start_node)

    table = PrettyTable()
    table.field_names = ["Кінцева вершина", "Найкоротший шлях", "Довжина шляху"]
    table.align["Найкоротший шлях"] = "l"

    for destination, path in shortest_paths.items():
        length = shortest_path_lengths[destination]
        table.add_row([destination, " -> ".join(path), length])

    print(table)
