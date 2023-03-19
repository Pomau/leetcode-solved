# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.res = []
        self.dfs(root, None, 0, x, y)
        return self.res[0][0] == self.res[1][0] and self.res[0][1] != self.res[1][1]
    def dfs(self, root, pred, depth, x, y):
        if root == None:
            return
        if root.val == x or root.val == y:
            self.res.append([depth, pred])
        self.dfs(root.left, root.val, depth + 1, x, y)
        self.dfs(root.right, root.val, depth + 1, x, y)