"""
Завдання 3: Вивід найкоротших шляхів з заданої верешини
"""

from queue import PriorityQueue
from prettytable import PrettyTable


def single_source_dijkstra_path(G, source):
    shortest_paths = {source: [source]}
    distances = {node: float('inf') for node in G.nodes}
    distances[source] = 0
    # PriorityQueue для зручності в пошуку найближчої невідвіданої вершини
    pq = PriorityQueue()
    pq.put((0, source))

    while not pq.empty():
        current_distance, current_node = pq.get()
        for neighbor in G.neighbors(current_node):
            distance = G[current_node][neighbor]['weight']
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pq.put((new_distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return shortest_paths, distances


def print_shortest_paths_from_node(G, start_node):
    shortest_paths, shortest_path_lengths = single_source_dijkstra_path(G, start_node)

    table = PrettyTable()
    table.field_names = ["Кінцева вершина", "Найкоротший шлях", "Довжина шляху"]
    table.align["Найкоротший шлях"] = "l"

    for destination, path in shortest_paths.items():
        length = shortest_path_lengths[destination]
        table.add_row([destination, " -> ".join(path), length])

    print(table)
