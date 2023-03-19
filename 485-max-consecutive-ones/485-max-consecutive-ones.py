class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0 or r == len(nums) - 1:
                ans = max(ans, r - l + (nums[r] == 1))
                l = r + 1
        return ans