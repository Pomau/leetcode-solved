class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        maxn = 0
        now = 0
        for num in arr:
            if num % 2 == 1:
                now += 1
            else:
                now = 0
            maxn = max(maxn, now)
        return maxn >= 3