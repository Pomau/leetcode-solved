class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        k %= (len(grid) * len(grid[0]))
        x1 = k % len(grid[0])
        y1 = k // len(grid[0])
        i, j = 0, 0
        x, y = x1, y1
        while y < len(grid):
            ans[y][x] = grid[i][j]
            x += 1
            j += 1
            if x >= len(grid[0]):
                x = 0
                y += 1
            if j >= len(grid[0]):
                j = 0
                i += 1
        x = 0
        y = 0
        while i < len(grid):
            ans[y][x] = grid[i][j]
            x += 1
            j += 1
            if x >= len(grid[0]):
                x = 0
                y += 1
            if j >= len(grid[0]):
                j = 0
                i += 1
        return ans