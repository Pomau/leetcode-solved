class Solution:
    def countAndSay(self, n: int) -> str:
        now = str(1)
        for i in range(n - 1):
            ans = []
            l = 0
            while l < len(now):
                count = 1
                while l + 1 < len(now) and now[l] == now[l + 1]:
                    count += 1
                    l += 1
                ans.append(f"{count}{now[l]}")
                l += 1
            now = "".join(ans)
        return now
