class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for m in range(len(s)):
            answer = max(answer, self.getpalindrom(m, m, s), self.getpalindrom(m, m + 1, s), key=lambda x: len(x))
        return answer
    
    def getpalindrom(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l  -= 1
            r += 1
        return s[l + 1:r]
 
            
        