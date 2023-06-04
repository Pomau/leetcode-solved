class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.edges = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    self.edges[i].append(j)
                    self.edges[j].append(i)
        
        self.used = [False] * len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if not self.used[i]:
                self.dfs(i)
                ans += 1
        return ans
    
    def dfs(self, u):
        if self.used[u]:
            return
        self.used[u] = True
        for v in self.edges[u]:
            self.dfs(v)