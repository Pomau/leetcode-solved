class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (r + l) // 2
            if nums[m] >= nums[0]:
                l = m
            else:
                r = m
        middle = r
        if nums[0] > target:
            if middle == len(nums):
                return -1
            l2, r2 = middle, len(nums)
        else:
            l2, r2 = 0, middle, 
        while r2 - l2 > 1:
            m = (r2 + l2) // 2
            if nums[m] > target:
                r2 = m
            else:
                l2 = m
        if nums[l2] == target:
            return l2
        return -1