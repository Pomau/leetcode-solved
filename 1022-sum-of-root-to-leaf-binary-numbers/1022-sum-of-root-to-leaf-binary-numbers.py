# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    def dfs(self, root, k):
        if root == None:
            return 0
        if root.left == root.right == None:
            return 2 * k + root.val
        return self.dfs(root.left, 2 * k + root.val) + self.dfs(root.right, 2 * k + root.val)