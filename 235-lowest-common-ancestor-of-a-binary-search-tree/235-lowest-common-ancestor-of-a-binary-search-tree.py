# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.lca
    
    def dfs(self, root, ch1, ch2):
        if root == None:
            return (False, False)
        ll, rl = self.dfs(root.left, ch1, ch2)
        lr, rr = self.dfs(root.right, ch1, ch2)
        l_have = ll or lr
        r_have = rl or rr
        if root.val == ch1.val:
            l_have = True
        if root.val == ch2.val:
            r_have = True
        if l_have and r_have:
            self.lca = root
            l_have = r_have = False
        return (l_have, r_have)
