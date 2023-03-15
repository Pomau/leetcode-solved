# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = TreeNode()
        self.node = self.head
        self.dfs(root)
        return self.head.right
    
    def dfs(self, root):
        if root == None:
            return None
        self.dfs(root.left)
        self.node.right = TreeNode(root.val)
        self.node = self.node.right
        self.dfs(root.right)
        