class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = sums = nums[0]
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                sums += nums[r]
            else:
                sums = nums[r]
            ans = max(ans, sums)
        return ans