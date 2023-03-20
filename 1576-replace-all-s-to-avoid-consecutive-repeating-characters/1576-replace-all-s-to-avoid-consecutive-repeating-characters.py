class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        for r in range(len(s)):
            if s[r] == "?":
                while True:
                    target = random.randint(0, 25)
                    ch = chr(ord("a") + target)
                    if (len(ans) == 0 or ch != ans[-1]) and (len(s) <= r + 1 or ch != s[r + 1]):
                        ans.append(ch)
                        break
            else:
                ans.append(s[r])
        return "".join(ans)