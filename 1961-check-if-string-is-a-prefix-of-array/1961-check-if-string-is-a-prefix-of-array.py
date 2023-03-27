class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l = 0
        for i in range(len(words)):
            for ch in words[i]:
                if l == len(s):
                    return False
                if s[l] != ch:
                    return False
                l += 1
            if l == len(s):
                break
        return l == len(s)