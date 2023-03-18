"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.dfs(0, 0, len(grid),  len(grid))
    
    def dfs(self, x0, y0, x1, y1):
        next = False
        for x in range(x0, x1):
            for y in range(y0, y1):
                if self.grid[x][y] != self.grid[x0][y0]:
                    next = True
                    break
        if next:
            xm = (x1 + x0) // 2
            ym = (y1 + y0) // 2
            return Node(None, False,
                self.dfs(x0, y0, xm, ym),
                self.dfs(x0, ym, xm, y1),
                self.dfs(xm, y0, x1, ym),
                self.dfs(xm, ym, x1, y1)
            )
        return Node(self.grid[x0][y0], True, None, None, None, None)