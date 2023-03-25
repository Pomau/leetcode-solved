class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        for i, ch in enumerate(s):
            if i % 2 == 1:
                ans.append(chr(ord(s[i - 1]) + int(ch)))
            else:
                ans.append(ch)
        return "".join(ans)