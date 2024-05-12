"""
Завдання 1. Автоматичне створення графа та візуалізація
"""

from faker import Faker
import networkx as nx
import random
import matplotlib.pyplot as plt


def create_client_map_graph(n_places=10, n_connections=4):
    fake = Faker()
    places = [fake.unique.first_name() for _ in range(n_places)]
    G = nx.Graph()
    G.add_nodes_from(places)
    for place in places:
        connections = random.sample(places, random.randint(1, n_connections))
        for connected_place in connections:
            if connected_place != place:
                weight = random.randint(1, 10)
                G.add_edge(place, connected_place, weight=weight)
    return G


def plot_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degree_centrality = nx.degree_centrality(G)
    most_central_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:2]

    title = "Граф сполучення клієнтів для доставки їжі"
    info_text = (f"Кількість вершин: {num_nodes}\n"
                 f"Кількість ребер: {num_edges}\n"
                 f"Дві найбільш центральні вершини: {most_central_nodes[0]}, {most_central_nodes[1]}\n"
                 f"Центральність: {degree_centrality[most_central_nodes[0]]:.2f}, {degree_centrality[most_central_nodes[1]]:.2f}")

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    node_colors = ['lightcoral' if node in most_central_nodes else 'lightblue' for node in G]
    nx.draw_networkx(G, pos, node_size=200, with_labels=True, font_size=10, edge_color='gray', node_color=node_colors)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.text(0.5, -0.1, info_text, transform=plt.gca().transAxes, ha='center', fontsize=12)
    plt.axis('off')
    plt.show()
