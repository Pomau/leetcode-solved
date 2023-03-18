class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while r - l > 1:
            m = (r + l) // 2
            if m * m >= num:
                r = m
            else:
                l = m
        return r * r == num