"""
Завдання 2. Обхід графа в глибину та в ширину з порівняльною візуалізацією
"""

import networkx as nx
import matplotlib.pyplot as plt


def find_least_central_node(G):
    degree_centrality = nx.degree_centrality(G)
    return min(degree_centrality, key=degree_centrality.get)


def visualize_dfs_bfs_paths_from_node(G, start_node):
    
    dfs_path = nx.dfs_tree(G, source=start_node)
    bfs_path = nx.bfs_tree(G, source=start_node)
    
    pos = nx.spring_layout(G) 
    
    plt.figure(figsize=(16, 8))
    
    def draw_path(ax, path, color, title):
        nx.draw_networkx_nodes(G, pos, node_size=200, node_color='lightgrey', ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="gray", ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=path.edges, edge_color=color, width=2, ax=ax)
        
        ax.set_title(title)
        ax.axis('off')
    
    ax1 = plt.subplot(1, 2, 1)
    draw_path(ax1, dfs_path, 'lightblue', f'DFS шлях з точки {start_node}')

    ax2 = plt.subplot(1, 2, 2)
    draw_path(ax2, bfs_path, 'lightcoral', f'BFS шлях з точки {start_node}')
    
    plt.show()
