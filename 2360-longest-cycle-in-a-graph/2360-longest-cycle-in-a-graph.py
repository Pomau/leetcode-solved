class Node:
    def __init__(self, to=None, color=None, ind=float("inf")):
        self.to = to
        self.color = color
        self.ind = ind
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.nodes = [Node() for i in range(len(edges))]
        self.ans = -1
        for i, road in enumerate(edges):
            self.nodes[i].to = road
        for i in range(len(self.nodes)):
            if self.nodes[i].color is None:
                self.dfs(i, i, 1)
        return self.ans
    def dfs(self, u, color, ind):
        if u < 0:
            return
            
        if self.nodes[u].color != None:
            if self.nodes[u].color == color:
                # print(u, color, ind)
                self.ans = max(self.ans, ind - self.nodes[u].ind)
            return
        self.nodes[u].ind = ind
        self.nodes[u].color = color
        self.dfs(self.nodes[u].to, color, ind + 1)