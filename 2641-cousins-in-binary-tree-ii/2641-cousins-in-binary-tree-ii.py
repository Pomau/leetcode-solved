# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth = defaultdict(int)
        self.sums(root, 0)
        return self.dfs(root, 0, None)
    
    def sums(self, root, d):
        if root == None:
            return 
        self.depth[d] += root.val
        self.sums(root.left, d + 1)
        self.sums(root.right, d + 1)
    
    def dfs(self, root, d, p):
        if root == None:
            return None
        sums = 0
        if d != 0:
            if p.left != None:
                sums += p.left.val
            if p.right != None:
                sums += p.right.val
        else:
            sums += root.val
            
        return TreeNode(self.depth[d] - sums, self.dfs(root.left, d + 1, root), self.dfs(root.right, d + 1, root))