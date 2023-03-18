class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        povtor = 0
        n = 1
        nums.sort()
        for r, num in enumerate(nums):
            if nums[r] == nums[r - 1]:
                povtor = nums[r]
            if nums[r] == n:
                n += 1
        return [povtor, n]