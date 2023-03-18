class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.used = [[False] * len(self.grid[0]) for _ in range(len(self.grid))]
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == 1:
                    return self.dfs(x, y)
    def dfs(self, x, y):
        self.used[x][y] = True
        dx = [0,0, 1, -1]
        dy = [1, -1, 0, 0]
        answer = 0
        for k in range(4):
            x2 = x + dx[k]
            y2 = y + dy[k]
            if not(0 <= x2 < len(self.grid) and 0 <= y2 < len(self.grid[0])) or self.grid[x2][y2] == 0:
                answer += 1
                continue
            if not self.used[x2][y2]:
                answer += self.dfs(x2, y2)
        return answer
