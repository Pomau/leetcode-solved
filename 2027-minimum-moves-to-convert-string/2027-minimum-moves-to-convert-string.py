class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        l = 0
        while l < len(s):
            if s[l] == "X":
                l += 3
                ans += 1
            else:
                l += 1
        return ans