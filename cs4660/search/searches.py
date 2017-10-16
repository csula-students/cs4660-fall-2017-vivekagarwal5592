"""
Searches module defines all different search algorithms
"""

def bfs(graph, initial_node, dest_node):
    Q = []
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q.append(initial_node)
    parent[initial_node] = None
    nodes_distance[initial_node] = 0
    last_node = dest_node
    visited_nodes.append(initial_node)
    while (bool(Q)):
        current_node = Q.pop(0)
        for neighbor in graph.neighbors(current_node):
            if (neighbor not in visited_nodes):
                    Q.append(neighbor)
                    nodes_distance[neighbor] = nodes_distance[current_node] + graph.distance(current_node,neighbor)
                    parent[neighbor] = current_node
                    visited_nodes.append(neighbor)
        if (dest_node in visited_nodes):
            break

    list = []
    while parent[last_node] is not None:
        list = [graph.get_edge(parent[last_node],last_node)]+ list
        last_node = parent[last_node]

    return list


def dfs(graph, initial_node, dest_node):
    Q = []
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q.append(initial_node)
    parent[initial_node] = None
    nodes_distance[initial_node] = 0
    last_node = dest_node
    visited_nodes.append(initial_node)
    while (bool(Q)):
        current_node = Q[0]
        all_neigbors_visited = True
        neighbors = graph.neighbors(current_node)
        neighbors.sort(key=lambda x: x.data)
        for n in neighbors:
            if (n not in visited_nodes):
                all_neigbors_visited = False
                Q = [n] +Q
                nodes_distance[n] = nodes_distance[current_node] + graph.distance(current_node, n)
                parent[n] = current_node
                visited_nodes.append(n)
                break
        if (all_neigbors_visited):
            Q.pop(0)
        if (dest_node in visited_nodes):
            break

    list = []
    while parent[last_node] is not None:
        list = [graph.get_edge(parent[last_node], last_node)] + list
        last_node = parent[last_node]

    return list


def dijkstra_search(graph, initial_node, dest_node):
    Q = {}
    visited_nodes = []
    grey_nodes = []
    parent = {}
    nodes_distance = {}
    Q[initial_node] = 0
    parent[initial_node] = None
    nodes_distance[initial_node] = 0
    last_node = dest_node
    visited_nodes.append(initial_node)
    while (bool(Q)):
        current_node = min(Q, key=Q.get)
        Q.pop(current_node)
        visited_nodes.append(current_node)
        for neighbor in graph.neighbors(current_node):
            if ((neighbor not in visited_nodes and neighbor not in grey_nodes) or (nodes_distance[neighbor]>nodes_distance[current_node] + graph.distance(current_node, neighbor))):
                Q[neighbor] = nodes_distance[current_node] + graph.distance(current_node, neighbor)
                nodes_distance[neighbor] = nodes_distance[current_node] + graph.distance(current_node, neighbor)
                parent[neighbor] = current_node
                grey_nodes.append(neighbor)

        if (dest_node in visited_nodes):
            break

    list = []
    while parent[last_node] is not None:
        list = [graph.get_edge(parent[last_node], last_node)] + list
        last_node = parent[last_node]



    return list


def a_star_search(graph, initial_node, dest_node):

    Q = {}
    hc = {}
    visited_nodes = []
    grey_nodes = []
    parent = {}
    nodes_distance = {}
    Q[initial_node] = 0
    hc[initial_node] = get_Euclidean_distance(initial_node, dest_node)
    parent[initial_node] = None
    nodes_distance[initial_node] = 0
    last_node = dest_node
    visited_nodes.append(initial_node)
    while (bool(Q)):
        current_node = min(hc, key=hc.get)
        hc.pop(current_node)
        Q.pop(current_node)
        visited_nodes.append(current_node)

        for neighbor in graph.neighbors(current_node):
            if ((neighbor not in visited_nodes and neighbor not in grey_nodes) or (nodes_distance[neighbor]>nodes_distance[current_node] + graph.distance(current_node, neighbor))):
                Q[neighbor] = nodes_distance[current_node] + graph.distance(current_node, neighbor)
                hc[neighbor] = get_Euclidean_distance(neighbor, dest_node) + graph.distance(current_node, neighbor)
                nodes_distance[neighbor] = nodes_distance[current_node] + graph.distance(current_node, neighbor)
                parent[neighbor] = current_node
                grey_nodes.append(neighbor)

        if (dest_node in visited_nodes):
            break

    list = []
    while parent[last_node] is not None:

        list = [graph.get_edge(parent[last_node], last_node)] + list
        last_node = parent[last_node]

    return list



def get_heuristic_cost(node1,node2):
    xdifference= abs(node1.data.x-node2.data.x)
    ydifference =abs(node1.data.y - node2.data.y)
    return xdifference + ydifference

def get_Euclidean_distance(node1,node2):
    xdifference = ((node1.data.x - node2.data.x) ** 2)
    ydifference = ((node1.data.y - node2.data.y) ** 2)
    dis = ((xdifference + ydifference)**0.5)
    return dis


