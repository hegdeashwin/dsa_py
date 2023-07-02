"""
Write a class to represent Adjacency List for Undirected Graph
"""


class Undirected_Adjacency_List:
    def __init__(self):
        self.nodes = []
        self.adjacency_list = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, srcNode, destNode):
        if srcNode not in self.nodes and destNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")
        
        temp = []
        if srcNode not in self.adjacency_list:
            temp.append(destNode)
            self.adjacency_list[srcNode] = temp
        else:
            self.adjacency_list[srcNode].append(destNode)
        
        temp = []
        if destNode not in self.adjacency_list:
            temp.append(srcNode)
            self.adjacency_list[destNode] = temp
        else:
            self.adjacency_list[destNode].append(srcNode)

    def print_graph_representation(self):
        for node in self.adjacency_list:
            print(node, " --> ", self.adjacency_list[node])

graph = Undirected_Adjacency_List()

graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 4)
graph.add_edge(1, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph_representation()
