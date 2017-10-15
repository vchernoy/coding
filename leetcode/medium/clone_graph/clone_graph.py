
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        graph = {}
        copy = self.clone(node, graph)
        return copy

    def clone(self, node, graph):
        if node is None:
            return None
        if node in graph:
            return graph[node]
            
        copy = UndirectedGraphNode(node.label)
        graph[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(self.clone(n, graph))
            
        return copy

