class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        minn = []
        maxn = []
        for i in range(len(nums)):
            minn.append(nums[i])
            maxn.append(nums[i])
            if len(minn) == 3:
                minn.sort()
                minn.pop()
                maxn.sort(reverse=True)
                maxn.pop()
        return maxn[0] * maxn[1] - minn[0] * minn[1]