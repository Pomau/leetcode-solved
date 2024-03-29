class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0:
                    if i == j:
                        continue
                    if i == 0:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]