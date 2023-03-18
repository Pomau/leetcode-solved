class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            now = [1]
            for pr_i in range(1, len(res[-1])):
                now.append(res[-1][pr_i] + res[-1][pr_i - 1])
            now.append(1)
            res.append(now)
        return res
        