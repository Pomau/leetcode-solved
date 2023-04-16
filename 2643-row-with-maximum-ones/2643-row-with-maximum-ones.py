class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        maxn = 0
        for i, row in enumerate(mat):
            now = 0
            for num in row:
                now += num
            if now > maxn:
                ans = i
                maxn = now
        return [ans, maxn]