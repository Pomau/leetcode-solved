class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = 0
        sums = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] > 0:
                sums += nums[i]
                res += 1
            elif sums + nums[i] > 0:
                res += 1
                sums += nums[i]
        return res