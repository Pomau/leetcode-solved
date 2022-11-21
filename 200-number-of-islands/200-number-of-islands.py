class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n, self.m = len(grid), len(grid[0])
        self.used = [[False] * self.m for _ in range(self.n)]
        self.grid = grid
        answer = 0
        for i in range(self.n):
            for j in range(self.m):
                if not self.used[i][j] and self.grid[i][j] == "1":
                    answer += 1
                    self.DFS(i, j)
        return answer
    
    def DFS(self, x, y):
        self.used[x][y] = True
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(len(dx)):
            x2 = x + dx[k]
            y2 = y + dy[k]
            if 0 <= x2 < self.n and 0 <= y2 < self.m and not self.used[x2][y2] and self.grid[x2][y2] == "1":
                self.DFS(x2, y2)
        