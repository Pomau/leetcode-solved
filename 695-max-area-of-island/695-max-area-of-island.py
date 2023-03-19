class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.used = [[False] * len(grid[0]) for _ in range(len(grid))]
        answer = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                answer = max(answer, self.dfs(x, y))
        return answer
    
    def dfs(self, x, y):
        if not (0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])) or self.used[x][y] or self.grid[x][y] != 1:
            return 0
        self.used[x][y] = True
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        answer = 1
        for k in range(len(dx)):
            x2 = x + dx[k]
            y2 = y + dy[k]
            answer += self.dfs(x2, y2)
        return answer