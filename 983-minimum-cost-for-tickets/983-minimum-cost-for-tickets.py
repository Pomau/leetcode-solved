class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.dp = [float("inf")] * (max(days) + 1)
        self.dp[0] = 0
        ask = set(days)
        for i in range(1, len(self.dp)):
            if i in ask:
                self.dp[i] = min(
                    self.dp[max(i - 1, 0)] + costs[0],
                    self.dp[max(i - 7, 0)] + costs[1],
                    self.dp[max(i - 30, 0)] + costs[2])
            else:
                self.dp[i] = self.dp[i - 1]
        return self.dp[-1]