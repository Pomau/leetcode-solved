# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        ans = 0
        if root.left != None:
            ans += root.left.val
        if root.right != None:
            ans += root.right.val
        return root.val == ans