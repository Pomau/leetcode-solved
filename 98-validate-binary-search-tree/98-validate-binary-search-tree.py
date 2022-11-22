# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root, float("-inf"), float("inf"))
    def DFS(self, root, lower, upper):
        if root is None:
            return True
        return (lower < root.val < upper) and self.DFS(root.left, lower, min(upper, root.val)) and self.DFS(root.right, max(lower, root.val), upper)
        