# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root)
    
    def DFS(self, node:TreeNode) -> int:
        if node is None:
            return 0
        depth_l = self.DFS(node.left)
        depth_r = self.DFS(node.right)
        depth = min(depth_l, depth_r)
        if depth == 0 and depth_l != depth_r:
            depth = max(depth_l, depth_r)
        return depth + 1
        
        