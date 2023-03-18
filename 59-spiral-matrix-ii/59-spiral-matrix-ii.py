class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        x, y, di = 0, 0, 0
        now = 1
        res[0][0] = now
        while now < n * n:
            x2, y2 = x + dx[di], y + dy[di]
            if 0 <= x2 < n and 0 <= y2 < n and res[y2][x2] == 0:
                x = x2
                y = y2
                now += 1
                res[y][x] = now
            else:
                di = (di + 1) % 4
        return res
            