# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._isSymmetric(root.left, root.right)
    
    def _isSymmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)
        