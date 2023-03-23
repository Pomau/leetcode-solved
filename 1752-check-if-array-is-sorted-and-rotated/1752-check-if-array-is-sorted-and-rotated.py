class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if nums[i] < nums[k]:
                k = i
        for i in range(len(nums)):
            if nums[i] == nums[k] and self.sol(i, nums):
                return True
        return False
    def sol(self, k, nums):
        for i in range(len(nums) - 1):
            if nums[(i + k)%len(nums)] > nums[(i + k + 1)%len(nums)]:
                return False
        return True
        