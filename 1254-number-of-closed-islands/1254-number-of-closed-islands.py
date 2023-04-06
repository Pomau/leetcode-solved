class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.color = [[-1] * len(grid[0]) for _ in range(len(grid))]
        self.grid = grid
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.color[i][j] == -1 and self.bfs(i, j, 1):
                    print(i, j)
                    ans += 1
        return ans
    def bfs(self, i, j, color):
        self.color[i][j] = color
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        ans = not (i == 0 or i == len(self.grid) - 1 or j == 0 or j == len(self.grid[0]) - 1)
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] == 0 and self.color[x][y] == -1:
                ans = self.bfs(i+dx[k], j+dy[k], color) and ans
        return ans