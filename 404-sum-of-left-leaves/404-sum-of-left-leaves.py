# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, False)
    def dfs(self, root, left):
        if root == None:
            return 0
        if root.left == None and root.right == None and left:
            return root.val
        return self.dfs(root.left, True) + self.dfs(root.right, False)