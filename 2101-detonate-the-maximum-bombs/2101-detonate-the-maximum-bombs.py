class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if self.is_damage(bombs[i][0], bombs[i][1], bombs[i][2], bombs[j][0], bombs[j][1]):
                    self.graph[i].append(j)
        ans = 0
        self.used = [False] * len(bombs)
        for i in range(len(bombs)):
            self.dfs(i)
            now = 0
            for i in range(len(bombs)):
                if self.used[i]:
                    self.used[i] = False
                    now += 1
            ans = max(ans, now)
        return ans
                    
    
    def dfs(self, u):
        if self.used[u]:
            return
        self.used[u] = True
        for v in self.graph[u]:
            self.dfs(v)
    
    def is_damage(self, x1, y1, r1, x2, y2):
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return r1 ** 2 >= dist