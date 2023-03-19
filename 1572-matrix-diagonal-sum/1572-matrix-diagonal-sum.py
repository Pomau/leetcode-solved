class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        n = len(mat)
        for i in range(n):
            answer += mat[i][i] + mat[i][n - i - 1]
            if i == n - i - 1:
                answer -= mat[i][i]
        return answer