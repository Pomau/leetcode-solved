class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 1
        if s.count("A") >= 2:
            return False
        for l in range(1, len(s)):
            if s[l] == s[l - 1]:
                count += 1
                if s[l] == "L" and count >= 3:
                    return False
            else:
                count = 1
        return True