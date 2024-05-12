from utils.task_1 import create_client_map_graph, plot_graph
from utils.task_2 import find_least_central_node, visualize_dfs_bfs_paths_from_node
from utils.task_3 import print_shortest_paths_from_node


if __name__ == '__main__':
    # Завдання 1
    G = create_client_map_graph()
    plot_graph(G)
    # Завдання 2
    start_node = find_least_central_node(G)
    visualize_dfs_bfs_paths_from_node(G, start_node)
    # Завдання 3
    print("Завдання 3: пошук найкоротших шляхів з вершини {start_node}")
    print_shortest_paths_from_node(G, start_node)
