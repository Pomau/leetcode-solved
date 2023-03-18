class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mink = float("inf")
        st = 1
        for i in range(len(nums)):
            st += nums[i]
            mink = min(mink, st)
            print(mink, st)
        if mink <= 0:
            st = 1 + abs(mink) + 1
        else:
            st = 1
        return st