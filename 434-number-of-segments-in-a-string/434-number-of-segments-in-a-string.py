class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        word = False
        for l, ch in enumerate(s):
            if ch != " ":
                word = True
            if (ch == " " or len(s) == l + 1) and word == True:
                word = False
                count += 1
        return count