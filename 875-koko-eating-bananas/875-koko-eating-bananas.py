class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) * h
        while r - l > 1:
            m = (r + l) // 2
            if self.check(piles, m) > h:
                l = m
            else:
                r = m
        return r
    def check(self, piles, k):
        hours = 0
        for pile in piles:
            hours += pile // k
            if pile % k != 0:
                hours += 1
        return hours