# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root)
    def traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.traversal(root.left) + [root.val] + self.traversal(root.right)