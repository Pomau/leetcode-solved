# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        root, maxDiameter = self.maxDiameterTree(root)
        return maxDiameter
    
    def maxDiameterTree(self, root):
        if root is None:
            return (0, 0)
        left, l_max = self.maxDiameterTree(root.left)
        right, r_max = self.maxDiameterTree(root.right)
        return(max(left, right) + 1, max([l_max, r_max, right + left]))