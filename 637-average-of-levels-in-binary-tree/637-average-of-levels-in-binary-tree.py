# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.count_depth = []
        self.sums_depth = []
        self.answer = []
        self.DFS(root, 0)
        for i in range(len(self.count_depth)):
            self.answer.append(self.sums_depth[i] / self.count_depth[i])
        return self.answer
        
    def DFS(self, u: TreeNode, depth: int):
        if u is None:
            return
        if len(self.count_depth) == depth:
            self.count_depth.append(0)
            self.sums_depth.append(0)
        self.count_depth[depth] += 1
        self.sums_depth[depth] += u.val
        self.DFS(u.left, depth + 1)
        self.DFS(u.right, depth + 1)
        