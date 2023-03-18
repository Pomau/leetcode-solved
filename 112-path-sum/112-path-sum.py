# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None and targetSum == 0:
            return False
        return self.dfs(root, targetSum)
    def dfs(self, root, k):
        if root == None:
            return False
        k -= root.val
        if k == 0 and root.left == root.right == None:
            return True
        return self.dfs(root.left, k) or self.dfs(root.right, k)