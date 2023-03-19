class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [10**9] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(len(cost)):
            dp[i] += cost[i]
            for k in range(1, 3):
                if i + k >= len(dp):
                    break
                dp[i + k] = min(dp[i + k], dp[i])
        return dp[-1]

