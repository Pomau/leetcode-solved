class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        max_power = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                l = r
            else:
                max_power = max(max_power, r - l + 1)
        return max_power
        