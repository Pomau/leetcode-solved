# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.dfs(root)
        return height[1]

    def dfs(self, root):
        if root == None:
            return [0, True]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return [max(l[0], r[0]) + 1, (abs(r[0] - l[0]) <= 1) and l[1] and r[1]]