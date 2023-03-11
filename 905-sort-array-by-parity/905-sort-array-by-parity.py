class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for r, num in enumerate(nums):
            if num % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums