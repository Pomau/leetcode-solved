class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for i in t:
            if len(s) != l and s[l] == i:
                l += 1
        return (l == len(s))
        