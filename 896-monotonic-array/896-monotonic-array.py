class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr = [a for a in nums]
        arr.sort()
        os1 = True
        for i in range(len(nums)):
            if nums[i] != arr[i]:
                os1 = False
        os2 = True
        arr.reverse()
        for i in range(len(nums)):
            if nums[i] != arr[i]:
                os2 = False
        return os1 or os2