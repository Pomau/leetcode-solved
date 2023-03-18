# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.result = []
        self.hash = defaultdict(list)
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if root == None:
            return "#"
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        hash_root = f"{l}, {root.val}, {r}"
        ind = 0
        have = False
        while ind < len(self.hash[hash_root]):
            if self.check(root, self.hash[hash_root][ind][1]):
                have = True
                if self.hash[hash_root][ind][0] == False:
                    self.result.append(root)
                    self.hash[hash_root][ind][0] = True
            ind += 1

        if not have:
            self.hash[hash_root].append([False, root])
        return hash_root
    
    def check(self, root, root2):
        if root == None and root2 == None:
            return True
        elif root == None or root2 == None or root.val != root2.val:
            return False
        return self.check(root.left, root2.left) and self.check(root.right, root2.right)
