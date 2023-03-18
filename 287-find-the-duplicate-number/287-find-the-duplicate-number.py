class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0:
                number = nums[i] - 1
                if nums[number] > 0:
                    nums[i] = nums[number]
                    nums[number] = -1
                else:
                    return number + 1
# -1 -1 -1 -1 2
        