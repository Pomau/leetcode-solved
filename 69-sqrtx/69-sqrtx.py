class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x + 1
        while r - l > 1:
            m = (r + l) // 2
            if m * m <= x:
                l = m
            else:
                r = m
        return l
        