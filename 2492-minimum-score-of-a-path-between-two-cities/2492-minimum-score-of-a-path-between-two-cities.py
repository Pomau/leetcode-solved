class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.roads = defaultdict(list)
        maxn = 0
        for road in roads:
            maxn = max(maxn, road[2])
            self.roads[road[0] - 1].append([road[1] - 1, road[2]])
            self.roads[road[1] - 1].append([road[0] - 1, road[2]])
        self.used = [False] * n
        return self.dfs(0)
    def dfs(self, u):
        if self.used[u]:
            return float("inf")
        self.used[u] = True
        mink = float("inf")
        for road in self.roads[u]:
            mink = min(self.dfs(road[0]), mink, road[1])
        return mink