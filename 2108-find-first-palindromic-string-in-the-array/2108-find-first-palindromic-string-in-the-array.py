class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == "".join(list(word)[::-1]):
                return word
        return ""