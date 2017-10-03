"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """

    f = open(file_path)
    data = f.read()
    data = data.split('\n')
   # print (data)
    for i in range(len(data)):
        if (i == 0):
          #  if(isinstance(graph, AdjacencyMatrix)):
           #     graph.initialize(int(data[i]))
            continue
        row = data[i].split(':')
        graph.add_node(Node(int(row[0])))
        graph.add_node(Node(int(row[1])))
        a = Node(int(row[0]))
        b = Node(int(row[1]))
        x = Edge(a,b,int(row[2]))
        graph.add_edge(x)

    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):

        return 'Node({})'.format(self.data)
    def __repr__(self):

        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):

        return self.data == other_node.data

    def __ne__(self, other):

        return not self.__eq__(other)

    def __hash__(self):

        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if (node_2 in self.adjacency_list[node_1]):
            return True
        else:
            return False

    def neighbors(self, node):
       return list(self.adjacency_list[node])

    def add_node(self, node):
        if (node in self.adjacency_list):
            return False
        else:
            self.adjacency_list[node] = {}
            return True

    def remove_node(self, node):
        if (node in self.adjacency_list):
            self.adjacency_list.pop(node)
            for i in self.adjacency_list.keys():
                if (node in self.adjacency_list[i]):
                    self.adjacency_list[i].pop(node)
            return True

        else:
            return False

    def add_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        if (to_node in self.adjacency_list[from_node]):
            return False
        else:
            self.adjacency_list[from_node][to_node] = edge.weight
         #   self.adjacency_list[to_node][from_node] = edge.weight
            return True

    def remove_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        if (to_node in self.adjacency_list[from_node]):
            self.adjacency_list[from_node].pop(to_node)
       #     self.adjacency_list[to_node].pop(from_node)
            return True
        else:
            return False

class AdjacencyMatrix(object):

   # def initialize(self,size):
    #    self.adjacency_matrix = [[0 for j in range(size)] for k in range(size)]

    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
       # self.adjacency_matrix = [[0 for j in range(11)] for k in range(11)]
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        index_from_node = self.__get_node_index(node_1)
        index_to_node = self.__get_node_index(node_2)
        if (self.adjacency_matrix[index_from_node][index_to_node] != 0):
            return True
        else:
            return False

    def neighbors(self, node):
        list = []
        index_node = self.__get_node_index(node)
        for i in range(len(self.adjacency_matrix[index_node])):
            if self.adjacency_matrix[index_node][i] != 0:
                list.append(self.nodes[i])
        list.sort(key=lambda x: x.data)
        return list

    def add_node(self, node):
        if node not in self.nodes:
            list = [0 for j in range(len(self.nodes))]
            self.adjacency_matrix.append(list)
            (self.nodes).append(node)
            for i in range(len(self.adjacency_matrix)):
                self.adjacency_matrix[i].append(0)
           # print(self.adjacency_matrix)

            return True
        else:
            return False


    def remove_node(self, node):
        if node in self.nodes:
            index_node = self.__get_node_index(node)
            (self.nodes).remove(node)
            self.adjacency_matrix.pop(index_node)
            for i in range(len(self.adjacency_matrix)):
                self.adjacency_matrix[i].pop(index_node)
            return True
        else:
            return False

    def add_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        index_from_node = self.__get_node_index(from_node)
        index_to_node = self.__get_node_index(to_node)
        if (self.adjacency_matrix[index_from_node][index_to_node] != edge.weight):
            self.adjacency_matrix[index_from_node][index_to_node] = edge.weight
         #   self.adjacency_matrix[to_node.data][from_node.data] = edge.weight
            return True
        else:
            return False

    def remove_edge(self, edge):
        from_node = edge.from_node
        to_node = edge.to_node
        index_from_node = self.__get_node_index(from_node)
        index_to_node = self.__get_node_index(to_node)
        if self.adjacency_matrix[index_from_node][ index_to_node] !=0:
            self.adjacency_matrix[index_from_node][ index_to_node] =0
            self.adjacency_matrix[index_to_node][index_from_node] = 0
            return True
        else:
            return False


    def __get_node_index(self, node):
        return self.nodes.index(node);
        pass

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for i in range(len(self.edges)):
            if self.edges[i].from_node == node_1 and self.edges[i].to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        list = []
        for i in range(len(self.edges)):
            if self.edges[i].from_node == node:
                list.append(self.edges[i].to_node)
        return list

    def add_node(self, node):
        if node not in self.nodes:
            (self.nodes).append(node)
            return True
        else:
            return False

    def remove_node(self, node):
        if node in self.nodes:
            (self.nodes).remove(node)
            for i in self.edges:
                if i.from_node == node or i.to_node == node:
                    self.remove_edge(i)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge not in self.edges:
            (self.edges).append(edge)
            return True
        else:
            return False

    def remove_edge(self, edge):
        if edge in self.edges:
            (self.edges).remove(edge)
            return True
        else:
            return False

