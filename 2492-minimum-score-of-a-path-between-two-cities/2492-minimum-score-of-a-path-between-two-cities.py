class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.roads = defaultdict(list)
        maxn = 0
        for road in roads:
            maxn = max(maxn, road[2])
            self.roads[road[0] - 1].append([road[1] - 1, road[2]])
            self.roads[road[1] - 1].append([road[0] - 1, road[2]])
        self.roads[0].sort(key= lambda x: x[1])
        self.used = [float("inf")] * n
        self.dfs(0, n - 1, maxn + 1)
        return self.used[n - 1]
    def dfs(self, u, target, cost):
        if self.used[u] <= cost:
            return True
        self.used[u] = cost
        for road in self.roads[u]:
            self.dfs(road[0], target, min(road[1], cost))
        