class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        i_d = 0
        x = 0
        y = -1
        answer = []
        while True:
            count = 0
            while 0 <= x + dx[i_d] < len(matrix) and 0 <= y + dy[i_d] < len(matrix[x]) and matrix[x + dx[i_d]][y + dy[i_d]] != -1000:
                x += dx[i_d]
                y += dy[i_d]
                answer.append(matrix[x][y]) 
                matrix[x][y] = -1000
                count += 1
            i_d = (i_d + 1) % 4
            if count == 0:
                break
        return answer
            
            
            
            
        