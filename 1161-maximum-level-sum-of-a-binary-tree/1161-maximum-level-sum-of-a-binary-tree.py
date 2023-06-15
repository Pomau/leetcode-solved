# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.weight = defaultdict(int)
        self.dfs(root, 0)
        maxn = 0
        for key in self.weight:
            if self.weight[key] > self.weight[maxn]:
                maxn = key
        return maxn + 1
        
    def dfs(self, root, depth):
        if root == None:
            return 
        self.weight[depth] += root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        