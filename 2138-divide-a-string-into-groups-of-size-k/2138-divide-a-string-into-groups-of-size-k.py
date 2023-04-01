class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [[]]
        for i, ch in enumerate(s):
            ans[-1].append(ch)
            if len(ans[-1]) == k:
                ans.append([])
        if len(ans[-1]) == 0:
            ans.pop()
        ans[-1].append(fill * (k - len(ans[-1])))
        return ["".join(i) for i in ans]