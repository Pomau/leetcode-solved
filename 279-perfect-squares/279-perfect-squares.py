class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        dp[0] = 0
        for i in range(len(dp)):
            for square in squares:
                if square +  i > n:
                    break
                dp[square + i] = min(dp[i] + 1, dp[square + i])
        return dp[n]
        