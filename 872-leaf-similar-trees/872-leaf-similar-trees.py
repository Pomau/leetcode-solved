# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        self.dfs(root1, r1)
        self.dfs(root2, r2)
        if len(r1) != len(r2):
            return False
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False
        return True
    def dfs(self, root, arr):
        if root == None:
            return 
        if root.left == root.right == None:
            arr.append(root.val)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)