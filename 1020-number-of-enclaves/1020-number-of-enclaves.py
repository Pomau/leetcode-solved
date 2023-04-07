class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans = 0
        self.grid = grid
        self.color = [[-1] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and self.color[i][j] == -1:
                    count, used = self.dfs(i, j, 1)
                    if used:
                        ans += count
        return ans
    def dfs(self, i, j, color):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        self.color[i][j] = color
        ans = [
            1,
            not (i == 0 or i == len(self.grid) - 1 or j == 0 or j == len(self.grid[0]) - 1)
        ]
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] == 1 and self.color[x][y] == -1:
                now = self.dfs(x, y, color)
                ans[1] = ans[1] and now[1]
                ans[0] += now[0]
        return ans