class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.isStr(firstWord) + self.isStr(secondWord) == self.isStr(targetWord)
    def isStr(self, s):
        ans = 0
        for ch in s:
            ans = ans * 10 + (ord(ch) - ord("a"))
        return ans