# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.DFS(root, p, q)[1]
    
    def DFS(self, root, p1, p2):
        if root == None:
            return (False, None)
        lc, findl = self.DFS(root.left, p1, p2)
        rc, findr = self.DFS(root.right, p1, p2)
        answer = None
        if findl != None:
            answer = findl
        if findr != None:
            answer = findr
        if lc and rc:
            answer = root
        if root in [p1, p2]:
            if lc or rc:
                answer = root
        return (lc or rc or root in [p1, p2], answer)
        
        