class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float("inf")
        for r, num in enumerate(nums):
            if r >= k - 1:
                ans = min(ans, num - nums[r - k + 1])
        return ans