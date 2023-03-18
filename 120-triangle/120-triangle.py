class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]
        for i in range(len(triangle)-1):
            ans = [float("inf") for _ in range(len(dp) + 1)]
            for j in range(len(dp)):
                ans[j] = min(ans[j], dp[j] + triangle[i + 1][j])
                ans[j + 1] = min(ans[j + 1], dp[j] + triangle[i + 1][j + 1])
            dp = ans
        return min(dp)
            