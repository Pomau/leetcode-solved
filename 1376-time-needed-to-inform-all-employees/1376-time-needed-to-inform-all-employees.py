class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.edges = defaultdict(list)
        self.times = informTime
        for i in range(n):
            if manager[i] == -1:
                continue
            self.edges[manager[i]].append(i)
        print(self.edges)
        return self.dfs(headID, 0)
    
    def dfs(self, v, time):
        ans = time + self.times[v]
        for i in self.edges[v]:
            ans = max(ans, self.dfs(i, time + self.times[v]))
        return ans