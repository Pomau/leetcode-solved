class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sums = sum(nums)
        nums.sort()
        ans = []
        now = 0
        for i in range(len(nums) - 1, -1, -1):
            now += nums[i]
            ans.append(nums[i])
            if now * 2 > sums:
                return ans
        return []