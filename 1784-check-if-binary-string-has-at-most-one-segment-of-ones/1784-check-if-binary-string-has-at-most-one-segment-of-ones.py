class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l = 0
        count = 0
        os = True
        for r in range(len(s)):
            if s[r] == "0":
                l = r + 1
            else:
                os = True
            if l > r and os:
                count += 1
            if s[r] == "0":
                os = False
        if s[r] == "1" and l != 0:
            count += 1
        return count  <= 1