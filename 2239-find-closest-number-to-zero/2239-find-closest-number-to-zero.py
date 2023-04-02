class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if abs(ans) > abs(num):
                ans = num
            if abs(ans) == abs(num) and num > ans:
                ans = num
        return ans