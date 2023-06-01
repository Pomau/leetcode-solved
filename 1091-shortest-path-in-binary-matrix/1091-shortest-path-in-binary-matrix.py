class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.dp = [[float("inf") for i in range(len(grid[0]))] for j in range(len(grid))]
        self.grid = grid
        q = [[0, 0, 1]]
        q_l = 0
        if self.grid[0][0] == 1:
            return -1
        while q_l < len(q):
            x, y, depth = q[q_l]
            q_l += 1
            if self.dp[x][y] <= depth:
                continue
            self.dp[x][y] = depth
            dx = [0, 0, 1, 1, 1, -1, -1, -1]
            dy = [1, -1, 0, -1, 1, 0, 1, -1]
            for k in range(len(dx)):
                x2, y2 = x + dx[k], y + dy[k]
                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and self.dp[x2][y2] > depth + 1 and self.grid[x2][y2] == 0:
                    q.append([x2, y2, depth + 1])
        if self.dp[-1][-1] == float("inf"):
            return -1
        return self.dp[-1][-1]
                    