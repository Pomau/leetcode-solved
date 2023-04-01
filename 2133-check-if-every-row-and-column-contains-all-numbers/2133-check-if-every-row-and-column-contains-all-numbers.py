class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        cols = [set() for i in range(len(matrix))]
        for i in range(len(matrix)):
            os = True
            row = set()
            for j in range(len(matrix)):
                cols[j].add(matrix[i][j] - 1)
                row.add(matrix[i][j] - 1)
            if len(row) != len(matrix):
                return False
        for col in cols:
            if len(col) != len(matrix):
                return False
        return True