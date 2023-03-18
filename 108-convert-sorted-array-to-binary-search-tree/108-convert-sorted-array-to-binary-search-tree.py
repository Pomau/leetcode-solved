# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.transformation(nums, 0, len(nums))
    
    def transformation(self, nums, l, r):
        if l >= r:
            return None
        if l + 1 == r:
            return TreeNode(nums[l])
        m = (r + l) // 2
        return TreeNode(nums[m], self.transformation(nums, l, m), self.transformation(nums, m + 1, r))
    
        