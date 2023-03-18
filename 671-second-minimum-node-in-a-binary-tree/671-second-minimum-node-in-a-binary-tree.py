# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root, root.val)
        if ans == float("inf"):
            ans = -1
        return ans
    def dfs(self, root, minx):
        if root == None:
            return float("inf")
        if minx != root.val:
            return root.val
        return min(self.dfs(root.left, minx), self.dfs(root.right, minx))