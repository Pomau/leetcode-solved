class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ch = [[0, i] for i in range(len(matrix))] + [[i, 0] for i in range(1, len(matrix[0]))]
        for i in range(len(ch)):
            x, y = ch[i]
            x2, y2 = x, y
            while 0 <= x2 < len(matrix[0]) and 0 <= y2 < len(matrix):
                if matrix[y2][x2] != matrix[y][x]:
                    return False
                x2 += 1
                y2 += 1
        return True