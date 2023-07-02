"""
Write a class to represent Adjacency Matrix for Directed Graph
"""

class Directed_Adjacency_Matrix:
    def __init__(self):
        self.nodes = []
        self.adjacency_matrix = []

    def init_adjacency_matrix(self):
        total_nodes = len(self.nodes)
        self.adjacency_matrix = [[0 for i in range(total_nodes)] for j in range(total_nodes)]

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, srcNode, destNode):
        self.adjacency_matrix[srcNode][destNode] = 1

    def print_graph_representation(self):
        print(self.adjacency_matrix)

graph = Directed_Adjacency_Matrix()

graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

graph.init_adjacency_matrix()

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 4)
graph.add_edge(1, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph_representation()
