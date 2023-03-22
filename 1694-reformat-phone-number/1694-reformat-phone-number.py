class Solution:
    def reformatNumber(self, number: str) -> str:
        ans = []
        for ch in number:
            if ch.isdigit():
                if len(ans) == 0 or len(ans[-1]) == 3:
                    ans.append(ch)
                else:
                    ans[-1] += ch
        if len(ans[-1]) == 1:
            bc = ans[-2][-1]
            ans[-2] = ans[-2][:-1]
            ans[-1] = bc + ans[-1]
        return "-".join(ans)