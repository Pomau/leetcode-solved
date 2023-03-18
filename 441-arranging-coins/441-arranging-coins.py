class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        k = 1
        while n >= 1 and n >= k:
            if n >= k:
                n -= k
            count += 1
            k += 1
        return count
                