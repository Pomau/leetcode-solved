class Solution:
    def checkString(self, s: str) -> bool:
        ind_a = -1
        b_first = float("inf")
        for i in range(len(s)):
            if s[i] == "a":
                ind_a = i
            else:
                b_first = min(i, b_first)
        return ind_a < b_first