class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        if n == 0:
            return 1
        dp[0] = 1
        squares = [i**2 for i in range(1, int(n ** 0.5) + 1)]
        for i in range(n):
            for square in squares:
                if i + square > n:
                    break
                dp[i + square] = min(dp[i + square], dp[i] + 1)
        return dp[n] - 1