class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.roads = [[] for i in range(n)]
        for road in edges:
            self.roads[road[0]].append(road[1])
            self.roads[road[1]].append(road[0])
        self.color = [None] * n
        color = 0
        for i in range(n):
            if self.color[i] is None:
                self.dfs(i, color)
                color += 1
        colors = [0] * color
        for i in range(n):
            colors[self.color[i]] += 1
        ans = 0
        sums = sum(colors)
        for i in colors:
            sums -= i
            ans += i * sums 
        return ans
    def dfs(self, u, color):
        if self.color[u] is not None:
            return
        self.color[u] = color
        for v in self.roads[u]:
            self.dfs(v, color)