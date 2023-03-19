class Solution:
    def balancedStringSplit(self, s: str) -> int:
        now = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == "R":
                now += 1
            else:
                now -= 1
            if now == 0:
                ans += 1
        return ans