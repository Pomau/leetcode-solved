class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ind = len(s)
        for i in range(len(s)):
            if s[i] == " ":
                k -= 1
                if k == 0:
                    ind = i
                    break
        return s[:ind]