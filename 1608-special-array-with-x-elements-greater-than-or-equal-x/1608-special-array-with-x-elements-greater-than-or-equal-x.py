class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        r = max(nums) + 1
        while r - l > 1:
            m = (r + l) // 2
            if self.check(nums, m) <= m:
                r = m
            else:
                l =m
        if self.check(nums, r) == r:
            return r
        return -1
            
    def check(self, nums, b):
        ans = 0
        for i in range(len(nums)):
            if nums[i] >= b:
                ans += 1
        return ans