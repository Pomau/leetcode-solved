class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (r + l) // 2
            if nums[m] >= nums[0]:
                l = m
            else:
                r = m
        if r == len(nums):
            return nums[0]
        return nums[r]