class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l = nums[0] - 1
        r = max(nums) + 1
        while r - l > 1:
            m = (r + l) // 2
            if self.check(nums, m):
                r = m
            else:
                l = m
        return r
    def check(self, nums, target):
        free = 0
        for r in range(len(nums)):
            if nums[r] > target:
                free -= nums[r] - target
            else:
                free += target - nums[r]
            if free < 0:
                # print(target, False)
                return False
        # print(target, True)
        return True