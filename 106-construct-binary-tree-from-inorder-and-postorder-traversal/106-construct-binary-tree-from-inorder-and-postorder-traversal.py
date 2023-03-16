# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        return self.dfs(0, len(inorder), 0, len(inorder))
    def dfs(self, l_in, r_in, l_post, r_post):
        if r_in == 0 or r_post == 0 or r_post < l_post or r_in < l_in:
            return None
        if r_in == l_in + 1:
            return TreeNode(self.inorder[l_in])
        root = TreeNode(self.postorder[r_post - 1])
        k = self.inorder.index(root.val)
        print(root.val, k, r_in, r_post - (r_in - (k + 1)), r_post - 1)
        print(root.val, l_in, k, l_post, r_post - (r_in - (k + 1)) - 1)
        root.right = self.dfs(k + 1, r_in, r_post - (r_in - (k + 1)), r_post - 1)
        root.left = self.dfs(l_in, k, l_post, r_post - (r_in - (k + 1)) - 1)
        return root