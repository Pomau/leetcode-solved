# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
                return self.dfs(root)[2]
    
    def dfs(self, root):
        if root == None:
            return [float("inf"), float("-inf"), float("inf")]
        l, r = self.dfs(root.left), self.dfs(root.right)
        return [min(l[0], r[0], root.val), max(l[1], r[1], root.val), min(l[2], r[2], abs(l[0] - root.val), abs(l[1] - root.val), abs(r[0] - root.val), abs(r[1] - root.val))]