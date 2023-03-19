class Solution:
    def freqAlphabets(self, s: str) -> str:
        r = 0
        result = []
        while r < len(s):
            if r + 2 < len(s) and s[r + 2] == "#":
                result.append(chr(ord("a")+int(s[r:r+2]) - 1))
                r += 3
            else:
                result.append(chr(ord("a")+int(s[r:r+1]) - 1))
                r += 1
        return ''.join(result)