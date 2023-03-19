class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        x = [0] * len(grid)
        y = [0] * len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ans += 1
                y[i] = max(y[i], grid[i][j])
                x[j] = max(x[j], grid[i][j])
        return sum(y) + sum(x) + ans