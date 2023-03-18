class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vow = ["a", "e", "i", "o", "u"]
        vow += [i.upper() for i in vow]
        ans = list(s)
        while l < r:
            while l < len(s) and s[l] not in vow:
                l += 1
            while r >= 0 and s[r] not in vow:
                r -= 1
            if l < r:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
        return "".join(ans)