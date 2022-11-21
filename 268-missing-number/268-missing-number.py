class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) + 1):
            if i < len(nums) and nums[i] <= len(nums):
                answer ^= nums[i]
            answer ^= i
        return answer