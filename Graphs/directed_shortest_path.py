"""
Write a class to show shortest path from source to destination node in an Directed Weighted Graph
Assume edge's weight to be 1
"""

from collections import defaultdict

class Directed_Shortest_Path:
    def __init__(self):
        self.nodes = []
        self.graph = defaultdict(list)
    
    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, srcNode, destNode, weight):
        if srcNode not in self.nodes or destNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")

        self.graph[srcNode].append((destNode, weight))
    
    def dfs(self, node, visited_nodes, stack):
        visited_nodes[node] = True
        
        if node in self.graph.keys():
            for n, weight in self.graph[node]:
                if visited_nodes[n] == False:
                    self.dfs(n, visited_nodes, stack)
    
        stack.append(node)
        return stack
    
    def find_shortest_path(self, srcNode):
        if srcNode not in self.nodes:
            raise Exception("Sorry, either source or destination nodes are do not exist!")
        
        totalNodes = len(self.nodes)
        
        visited_nodes = [False] * (totalNodes)
        stack = []
        s = []
        
        for i in range(totalNodes):
            if visited_nodes[i] == False:
                s = self.dfs(srcNode, visited_nodes, stack)
        
        distance = [float("Inf")] * (totalNodes)
        distance[srcNode] = 0
        
        while stack:
            i = stack.pop()
            
            for node, weight in self.graph[i]:
                if distance[node] > distance[i] + weight:
                    distance[node] = distance[i] + weight
            
        print(distance)
        
    def print_graph_representation(self):
        print(self.graph)
        for node in self.graph:
            print(node, " --> ", self.graph[node])

graph = Directed_Shortest_Path()

graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 6)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 4, 4)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, -1)
graph.add_edge(4, 5, -2)

graph.print_graph_representation()

graph.find_shortest_path(1)
