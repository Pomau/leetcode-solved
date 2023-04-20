# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.alf = defaultdict(list)
        self.dfs(root, 0, 0)
        ans = 1
        for key in self.alf.keys():
            self.alf[key].sort()
            if len(self.alf[key]) > 1:
                if key == 1:
                    ans = max(ans, 2)
                    continue
                os = 0
                if self.alf[key][0] < 0 and self.alf[key][-1] < 0 or self.alf[key][0] > 0 and self.alf[key][-1] > 0:
                    os += 1
                ans = max(ans, abs(self.alf[key][0] - self.alf[key][-1]) + os)
        # print(self.alf)
        return ans
    def dfs(self, root, k, d):
        if root == None:
            return 
        #print(root.val, d, k)
        self.alf[d].append(k)
        l, r = 2 * k, 2 * k
        if k > 0:
            r -= 1
        elif k < 0:
            l += 1
        if d == 0:
            l += 1
            r -= 1
        self.dfs(root.left, l, d + 1)
        self.dfs(root.right,r, d + 1)