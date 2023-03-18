class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = -1
        r = len(nums) - 1
        while r - l > 1:
            m = (r  + l) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        st = r
        if nums[r] != target:
            return [-1, -1]
        l = st
        r = len(nums)
        while r - l > 1:
            m = (r  + l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        return [st, l]