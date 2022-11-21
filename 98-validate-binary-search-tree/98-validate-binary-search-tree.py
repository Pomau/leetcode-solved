# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root, float("-inf"), float("inf"))
    def DFS(self, root, low, high):
        if root == None:
            return True
        if not (low < root.val < high):
            return False
        return self.DFS(root.left, low, min(high, root.val)) and self.DFS(root.right, max(low, root.val), high)
            
        