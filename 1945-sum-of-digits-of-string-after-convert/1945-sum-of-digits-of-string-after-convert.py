class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        for ch in s:
            now = ord(ch) - ord("a") + 1
            while now > 0:
                ans += now % 10
                now //= 10
        while k > 1:
            k -= 1
            now = 0
            while ans > 0:
                now += ans % 10
                ans //= 10
            ans = now
        return ans