# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.hash = defaultdict(set)
        self.dfs(root, False)
        ans = self.dfs(subRoot, True)
        for n in self.hash[hash(ans)]:
            if n == ans:
                return True
        return False
    
    def dfs(self, root, check=False):
        if root == None:
            return "#"
        answer = f"{root.val},{self.dfs(root.left)},{self.dfs(root.right)}"
        if  not check:
            self.hash[hash(answer)].add(answer)
        return answer