class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 0
        r = 10000000000000000000
        while r - l > 1:
            m = (r + l) // 2
            if self.check(ranks, m) >= cars:
                r = m
            else:
                l = m
        ans = 0
        for i in range(r - 100, r + 100):
            if i > 0 and self.check(ranks, i) >= cars:
                return i
        return r
    
    def check(self, ranks, time):
        ans = 0
        for i in range(len(ranks)):
            ans += int(sqrt(time // ranks[i]))
        return ans