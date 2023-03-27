class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = sum(nums)
        for l in range(len(nums)):
            suffix -= nums[l]
            if suffix == prefix:
                return l
            prefix += nums[l]
        return -1