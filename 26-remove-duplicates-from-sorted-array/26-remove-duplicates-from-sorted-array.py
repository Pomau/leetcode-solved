class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        count_unique = 0
        prew = -10 ** 10
        for r in range(len(nums)):
            if nums[r] != prew:
                nums[l] = nums[r]
                l += 1
                count_unique += 1
            prew = nums[r]
        return count_unique
        