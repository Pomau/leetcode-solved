# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        l = 0
        while q[l] != None:
            q.append(q[l].left)
            q.append(q[l].right)
            l += 1
        while l < len(q):
            if q[l] != None:
                return False
            l+=1
        return True