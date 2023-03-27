class Solution:
    def makeFancyString(self, s: str) -> str:
        word = []
        for r in range(0, len(s)):
            if len(word) < 2 or "".join(word[-2:]) != s[r] * 2:
                word.append(s[r])
        return "".join(word)
                