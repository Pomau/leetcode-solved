class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mink = float("inf")
        maxk = float("-inf")
        for i, num in enumerate(nums):
            mink = min(mink, num)
            maxk = max(maxk, num)
        return max(0, (maxk - k) - (mink+k))