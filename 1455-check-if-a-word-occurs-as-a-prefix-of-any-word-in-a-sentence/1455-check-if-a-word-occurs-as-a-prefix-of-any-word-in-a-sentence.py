class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if len(searchWord) > len(word):
                continue
            l = 0
            while l < len(searchWord):
                if word[l] != searchWord[l]:
                    break
                l += 1
            if l == len(searchWord):
                return i + 1
        return -1