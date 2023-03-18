# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while r - l > 1:
            m = (r + l) // 2
            if not isBadVersion(m):
                l = m
            else:
                r = m
        return r 