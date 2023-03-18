class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upp = 0
        for ch in word:
            if ch.upper() == ch:
                upp += 1
        return upp == len(word) or upp == 0 or upp == 1 and word[0].upper() == word[0]