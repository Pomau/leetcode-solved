class Solution:
    def maximumTime(self, time: str) -> str:
        ans = list(time)
        if ans[0] == "?":
            if ans[1] == "?" or int(ans[1]) <= 3:
                ans[0] = "2"
            else:
                ans[0] = "1"
        if ans[1] == "?":
            if ans[0] == "2":
                ans[1] = "3"
            else:
                ans[1] = "9"
        if ans[3] == "?":
            ans[3] = "5"
        if ans[4] == "?":
            ans[4] = "9"
        return "".join(ans)