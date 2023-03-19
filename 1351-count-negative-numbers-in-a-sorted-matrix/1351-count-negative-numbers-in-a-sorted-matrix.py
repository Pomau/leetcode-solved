class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        x = 0
        for y in range(len(grid) -1, -1, -1):
            while x < len(grid[y]) and grid[y][x] >= 0:
                x += 1
            ans += len(grid[y]) - x
        return ans