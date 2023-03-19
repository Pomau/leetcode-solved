# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, root.val)
    def dfs(self, root, val):
        if root == None:
            return True
        if root.val != val:
            return False
        return self.dfs(root.left, val) and self.dfs(root.right, val)