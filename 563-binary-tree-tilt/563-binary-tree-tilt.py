# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    def dfs(self, root):
        if root == None:
            return [0, 0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return [l[0] + r[0] + root.val, l[1] + r[1] + abs(l[0] - r[0])]