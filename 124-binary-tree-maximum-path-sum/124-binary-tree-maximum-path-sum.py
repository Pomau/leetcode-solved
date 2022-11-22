# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.DFS(root))
    
    def DFS(self, root):
        if root is None:
            return (0, float("-inf"))
        l, l_max = self.DFS(root.left)
        r, r_max = self.DFS(root.right)
        return (max(max(l, r) + root.val, root.val), max(l_max, r_max, l + r + root.val, root.val, max(l, r) + root.val))