class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        mink = float("inf")
        for num in nums:
            ans = max(ans, num - mink)
            mink = min(mink, num)
        if ans == 0:
            ans = -1
        return ans