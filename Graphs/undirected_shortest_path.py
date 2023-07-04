"""
Write a class to show shortest path from source to destination node in an Undirected Graph
Assume edge's weight to be 1
"""

from collections import defaultdict

class Undirected_Shortest_Path:
    def __init__(self):
        self.nodes = []
        self.graph = defaultdict(list)
    
    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, srcNode, destNode):
        if srcNode not in self.nodes or destNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")

        self.graph[srcNode].append(destNode)
        self.graph[destNode].append(srcNode)
    
    def find_shortest_path(self, srcNode, destNode):
        if srcNode not in self.nodes or destNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")
        
        totalNodes = len(self.nodes)
        visited_nodes = [False] * (totalNodes + 1)
        parent = [False] * (totalNodes + 1)
        queue = []
        
        queue.append(srcNode)
        visited_nodes[srcNode] = True
        
        # Required to backtack to parent node from destNode
        parent[srcNode] = -1
        
        while queue:
            frontNode = queue.pop(0)
            for i in self.graph[frontNode]:
                if visited_nodes[i] == False:
                    visited_nodes[i] = True
                    parent[i] = frontNode
                    queue.append(i)
        
        shortest_path = []
        currentNode = destNode
        shortest_path.append(currentNode)
        
        while currentNode != srcNode:
            currentNode = parent[currentNode]
            shortest_path.append(currentNode)
        
        shortest_path.reverse()
        print(f"Shortest path from node({srcNode}) to node({destNode}) is {shortest_path}")
        return shortest_path
        
    def print_graph_representation(self):
        for node in self.graph:
            print(node, " --> ", self.graph[node])

graph = Undirected_Shortest_Path()

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)
graph.add_node(8)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 8)
graph.add_edge(4, 6)
graph.add_edge(5, 8)
graph.add_edge(6, 7)
graph.add_edge(7, 8)

graph.print_graph_representation()

graph.find_shortest_path(1, 8)
