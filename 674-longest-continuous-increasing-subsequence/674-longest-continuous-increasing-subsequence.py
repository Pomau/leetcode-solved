class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        count = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num > nums[i - 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans