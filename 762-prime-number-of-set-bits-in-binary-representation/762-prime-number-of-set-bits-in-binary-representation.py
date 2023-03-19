class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
        ans = 0
        for i in range(left, right + 1):
            x = i
            now = 0
            while x > 0:
                now += x % 2
                x //= 2
            if now in prime:
                ans += 1
        return ans