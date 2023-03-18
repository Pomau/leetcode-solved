# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.used = set()
        return self.dfs(root, k) 

    def dfs(self, root, k):
        if root == None:
            return False
        if k - root.val in self.used:
            return True
        self.used.add(root.val)
        return self.dfs(root.left, k) or self.dfs(root.right, k)