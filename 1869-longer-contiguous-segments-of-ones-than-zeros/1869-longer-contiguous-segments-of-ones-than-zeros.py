class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return self.maxn(s, "0") < self.maxn(s, "1")
    def maxn(self, s, target):
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] != target:
                l = r + 1
            ans = max(ans, r - l + 1)
        return ans