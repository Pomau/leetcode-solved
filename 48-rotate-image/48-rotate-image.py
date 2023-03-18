class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for level in range(n // 2):
            for i in range(n - level * 2 - 1):
                now = matrix[n - 1 - level - i][level]
                matrix[n - 1 - level - i][level] = matrix[n - 1 - level][n - 1 - level - i]
                matrix[n - 1 - level][n - 1 - level - i] = matrix[level + i][n - 1 - level]
                matrix[level + i][n - 1 - level] = matrix[level][level + i]
                matrix[level][level + i] = now
            
        