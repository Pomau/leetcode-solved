class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        used = [[False] * cols for _ in range(rows)]
        ans = []
        q = [[rCenter, cCenter]]
        l = 0
        while len(q) > l:
            x, y = q[l]
            l += 1
            ans.append([x, y])
            used[x][y] = True
            dx = [0, 0, 1, -1]
            dy = [-1, 1, 0, 0]
            for k in range(len(dx)):
                x2 = x + dx[k]
                y2 = y + dy[k]
                if 0 <= x2 < rows and 0 <= y2 < cols and not used[x2][y2]:
                    used[x2][y2] = True
                    q.append([x2, y2])
        return ans