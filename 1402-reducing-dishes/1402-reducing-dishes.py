class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        ans = 0
        sums = 0
        now = 0
        for i, el in enumerate(satisfaction):
            now += el + sums
            sums += el
            ans = max(ans, now)
        return ans