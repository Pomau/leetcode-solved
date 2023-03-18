class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if n * m != r * c:
            return mat
        answer = [[0] * c for _ in range(r)]
        x, y = 0, 0
        for i in range(n):
            for j in range(m):
                if y >= c:
                    x += 1
                    y = 0
                answer[x][y] = mat[i][j]
                y += 1
        return answer