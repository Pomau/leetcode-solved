# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.arr = []
        self.dfs(root, 0)
        return self.arr
    def dfs(self, root, k):
        if root == None:
            return
        while len(self.arr) <= k:
            self.arr.append([])
        self.arr[k].append(root.val)
        self.dfs(root.left, k + 1)
        self.dfs(root.right, k + 1)