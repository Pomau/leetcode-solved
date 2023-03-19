class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (r + l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        if nums[l] == target:
            return l
        return -1