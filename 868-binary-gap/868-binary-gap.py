class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        k = 0
        now = float("-inf")
        while n > 0:
            t = n % 2
            n //= 2
            if t == 0:
                now += 1
            else:
                now = 1
                k += 1
            ans = max(ans, now)
        if k == 1:
            return 0
        return ans