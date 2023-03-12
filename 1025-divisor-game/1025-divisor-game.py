class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(2, len(dp)):
            j = False
            for k in range(1, i):
                if i % k == 0 and not dp[i - k]:
                    j = True
            dp[i] = j
        return dp[-1]
            