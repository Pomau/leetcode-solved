class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.n = len(board)
        self.m = len(board[0])
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "R":
                    dx = [0, 0, 1, -1]
                    dy = [1, -1, 0, 0]
                    for k in range(4):
                        count += self.dfs(i, j, board, dx[k], dy[k])
        return count
    def dfs(self, x, y, board, dx, dy):
        while 0 <= x < self.n and 0 <= y < self.m:
            if board[x][y] == "p":
                return 1
            if board[x][y] == "B":
                break
            x += dx
            y += dy
        return 0