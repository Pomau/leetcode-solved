class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ans = [m, n]
        for num in ops:
            ans = [min(ans[0], num[0]), min(ans[1], num[1])]
        return ans[0] * ans[1]