"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.nodes = {}
        if node == None:
            return None
        else:
            return self.clone(node)
    
    def clone(self, node):
        if node is None or node.val is None:
            return Node(0, [])
        if node.val in self.nodes:
            return self.nodes[node.val]
        node_new = Node(node.val)
        self.nodes[node.val] = node_new
        neighbors = []
        for neighbor in node.neighbors:
            neighbors.append(self.clone(neighbor))
        node_new.neighbors = neighbors
        self.nodes[node.val] = node_new
        return self.nodes[node.val]
        