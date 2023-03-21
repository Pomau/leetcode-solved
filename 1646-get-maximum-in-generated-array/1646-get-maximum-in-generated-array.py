class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 2)
        dp[1] = 1
        for i in range(1, n//2 + 1):
            dp[2*i] = dp[i]
            if 2 * i + 1 <= n:
                dp[2*i+1] = dp[i] + dp[i +1]
        return max(dp)