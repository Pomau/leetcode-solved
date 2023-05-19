class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.edges = [[] for i in range(len(graph))]
        for i in range(len(graph)):
            for u in graph[i]:
                self.edges[i].append(u)
        self.colors = [-1] * len(graph)
        self.ans = True
        
        for i in range(len(graph)):
            if self.colors[i] == -1:
                self.dfs(i, 0)
        return self.ans
    
    def dfs(self, u, color):
        if self.colors[u] == 1 - color:
            self.ans = False
            return
        if self.colors[u] != -1:
            return
        self.colors[u] = color
        for v in self.edges[u]:
            self.dfs(v, 1 - color)