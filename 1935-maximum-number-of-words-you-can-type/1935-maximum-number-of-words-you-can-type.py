class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken = False
        word = 0
        alf = set(brokenLetters)
        for i, ch in enumerate(text):
            if ch != " ":
                word += 1
                if ch in alf:
                    broken = True
            if (ch == " " or len(text) == i + 1) and word != 0:
                if not broken:
                    ans += 1
                broken = False
                word = 0
        return ans