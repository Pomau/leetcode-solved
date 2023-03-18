class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.valid(s, 2) <= 1
    
    def valid(self, s, k):
        if k < 0:
            return 1
        l = 0
        r = len(s) - 1
        os = 0
        while l < r:
            if s[l] != s[r]:
                os += 1 + min(self.valid(s[l + 1:r + 1], k - 1), self.valid(s[l:r], k - 1))
                l = r
            else:
                l += 1
                r -= 1
        return os