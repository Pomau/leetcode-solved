# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    def dfs(self, root, num):
        if root == None:
            return 0
        target = num * 10 + root.val
        if root.left == root.right == None:
            return target
        return self.dfs(root.left, target) + self.dfs(root.right, target)