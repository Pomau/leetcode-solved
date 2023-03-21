class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = -1
        for r in range(len(nums)):
            if nums[r] != 0:
                l = r
            else:
                ans += r - l
        return ans