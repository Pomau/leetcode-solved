class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        pust = 0
        while numBottles > 0:
            ans += numBottles
            pust, numBottles = (numBottles + pust) % numExchange, (numBottles + pust) // numExchange
        return ans