class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_end = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index_end] = nums[i]
                index_end += 1
        return index_end