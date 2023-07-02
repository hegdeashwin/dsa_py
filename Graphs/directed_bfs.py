"""
Write a class to traverse Directed Graph using BFS
"""

from collections import defaultdict

class Directed_BFS:
    def __init__(self):
        self.nodes = []
        self.graph = defaultdict(list)
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def add_edge(self, srcNode, destNode):
        if srcNode not in self.nodes or destNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")
        
        self.graph[srcNode].append(destNode)
    
    def bfs(self, startNode):
        if startNode not in self.nodes:
            raise Exception("Sorry, start node do not exist!")
        
        # Mark all nodes as not visited
        visited_nodes = [False] * len(self.nodes)

        # Create Queue
        queue = []

        visited_nodes[startNode] = True
        queue.append(startNode)

        while queue:
            s = queue.pop(0)

            print(s, end=" ")

            for i in self.graph[s]:
                if visited_nodes[i] == False:
                    visited_nodes[i] = True
                    queue.append(i)
    
    def print_graph_representation(self):
        for node in self.graph:
            print(node, " --> ", self.graph[node])

graph = Directed_BFS()

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

graph.bfs(2)

print('\n')

graph.bfs(0)