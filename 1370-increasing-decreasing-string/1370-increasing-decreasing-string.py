class Solution:
    def sortString(self, s: str) -> str:
        alf = [0] * 26
        for i in range(len(s)):
            alf[ord(s[i]) - ord('a')] += 1
        have = True
        ans = []
        while have:
            have = False
            for i in range(26):
                if alf[i] > 0:
                    have = True
                    ans.append(chr(ord("a") + i))
                    alf[i] -= 1
            for i in range(25, -1, -1):
                if alf[i] > 0:
                    have = True
                    ans.append(chr(ord("a") + i))
                    alf[i] -= 1
        return "".join(ans)