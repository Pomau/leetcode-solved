class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]
        ans = 0
        for i in range(len(mat)):
            if rows[i] != 1:
                continue
            for j in range(len(mat[0])):
                if cols[j] != 1 or mat[i][j] != 1:
                    continue
                ans += 1
        return ans
                