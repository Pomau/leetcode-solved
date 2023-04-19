# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.bfs(root, 0, 0), self.bfs(root, 1, 0)) - 1
    
    def bfs(self, root, turn, depth):
        if root == None:
            return depth
        # print(root.val)
        node = root.left
        other = root.right
        if turn == 0:
            node = root.right
            other = root.left
        
        return max(self.bfs(node, 1 - turn, depth + 1), self.bfs(other, turn, 1))