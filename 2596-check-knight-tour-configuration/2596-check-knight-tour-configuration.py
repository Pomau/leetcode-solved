class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        dx = [1, -1, 1, -1, 2, -2, 2, -2]
        dy = [2, -2, -2, 2, 1, -1, -1, 1]
        hods = [[dx[i], dy[i]] for i in range(len(dx))] 
        alf = {}
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                alf[grid[i][j]] = [i, j]
        now = 0
        x, y = 0, 0
        while now != n * m - 1:
            now += 1
            x1, y1 = alf[now]
            if [x1-x, y1-y] not in hods:
                return False
            x, y, = x1, y1
        return True