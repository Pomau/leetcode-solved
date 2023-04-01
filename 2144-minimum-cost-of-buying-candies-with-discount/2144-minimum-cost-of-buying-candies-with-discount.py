class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort()
        k = 0
        for i in range(len(cost) - 1, -1, -1):
            ans += cost[i]
            k += 1
            if k == 3:
                k = 0
                ans -= cost[i]
        return ans