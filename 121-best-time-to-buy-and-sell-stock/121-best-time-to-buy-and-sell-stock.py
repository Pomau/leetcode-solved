class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prefix = prices[0]
        for i in range(1, len(prices)):
            min_prefix = min(min_prefix, prices[i])
            max_profit = max(prices[i] - min_prefix, max_profit)
        return max_profit
                                
        