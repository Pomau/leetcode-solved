class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.edges = [[] for _ in range(len(colors))]
        self.used = [False for _ in range(len(colors))]
        self.cols = [-1 for _ in range(len(colors))]
        dp = [defaultdict(int) for i in range(len(colors))]
        self.colors = colors
        for edge in edges:
            self.edges[edge[0]].append(edge[1])
        self.topologic = []
        self.os = False
        for i in range(len(colors)):
            if self.cols[i] == -1:
                self.find_cycle(i)
        for i in range(len(colors)):
            if not self.used[i]:
                self.top(i)
        if self.os:
            return -1
        ans = 0
        for i in range(len(colors)):
            now = self.topologic[i]
            for edge in self.edges[now]:
                for color in dp[edge].keys():
                    dp[now][color] = max(dp[now][color], dp[edge][color])
                    ans = max(ans, dp[now][color])
            dp[now][colors[now]] += 1
            ans = max(ans, dp[now][colors[now]])
        # print(self.topologic, self.os, dp)
        return ans
    def find_cycle(self, u):
        self.cols[u] = 1
        #print("Входим", u)
        for edge in self.edges[u]:
           # print(u, edge)
            if self.cols[edge] == 1:
                #print(u, edge)
                self.os = True
                return
            if self.cols[edge] == 2:
                continue
            self.find_cycle(edge)
        self.cols[u] = 2
        # print("Выходим", u)
    
    def top(self, u):
        if self.used[u]:
            return 
        self.used[u] = True
        for edge in self.edges[u]:
            self.top(edge)
        self.topologic.append(u)
    