class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.roads = [[] for i in range(n)]
        for road in connections:
            self.roads[road[0]].append(road[1])
            self.roads[road[1]].append(road[0])
        ans = 0
        self.used = [False] * n
        for i in range(n):
            if not self.used[i]:
                self.dfs(i)
                ans += 1
        if n > len(connections) + 1:
            return -1
        return ans - 1
    def dfs(self, u):
        self.used[u] = True
        for v in self.roads[u]:
            if not self.used[v]:
                self.dfs(v)
