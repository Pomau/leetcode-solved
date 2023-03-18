# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.answer = []
        self.dfs(root, [])
        return self.answer
    
    def dfs(self, root, path):
        if root == None:
            return
        path.append(str(root.val))
        if root.left == root.right == None:
            self.answer.append("->".join(path))
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()