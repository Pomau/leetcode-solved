class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.colors = [-1] * n
        self.roads = [[] for _ in range(n)]
        for edge in edges:
            self.roads[edge[0]].append(edge[1])
            self.roads[edge[1]].append(edge[0])
        self.dfs(source, source)
        return self.colors[source] == self.colors[destination]

    def dfs(self, u, color):
        if self.colors[u] != -1:
            return
        self.colors[u] = color
        for road in  self.roads[u]:
            self.dfs(road, color)