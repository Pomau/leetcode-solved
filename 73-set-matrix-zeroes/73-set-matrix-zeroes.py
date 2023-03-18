import random 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_number = 1
        while self.haveNumberMatrix(matrix, new_number):
            new_number = random.randint(0, 2**31 - 1)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    for k in range(4):
                        x2 = x
                        y2 = y
                        while 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[x2]):
                            if matrix[x2][y2] != 0:
                                matrix[x2][y2] = new_number
                            x2 += dx[k]
                            y2 += dy[k]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == new_number:
                    matrix[x][y] = 0
                    
        
    def haveNumberMatrix(self, matrix, k):
        for i in matrix:
            for j in i:
                if j == k:
                    return True
        return False