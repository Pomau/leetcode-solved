class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float("-inf")
        sums = 0
        for r, num in enumerate(nums):
            sums += num
            if r >= k:
                sums -= nums[r - k]
            if r >= k - 1:
                ans = max(ans, sums / k)
        return ans