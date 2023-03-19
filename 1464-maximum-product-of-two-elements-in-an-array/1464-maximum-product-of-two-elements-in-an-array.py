class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn = sorted(nums, reverse=True)[:2]
        return (maxn[0] -1) * (maxn[1] - 1)