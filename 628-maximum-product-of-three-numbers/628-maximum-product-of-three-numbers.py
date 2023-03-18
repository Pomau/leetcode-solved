class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxn = []
        minn = []
        for num in nums:
            maxn.append(num)
            maxn.sort(reverse=True)
            minn.append(num)
            minn.sort()
            if len(maxn) == 4:
                maxn.pop()
            if len(minn) == 3:
                minn.pop()
        return max(maxn[0] * maxn[1] * maxn[2], minn[0] * minn[1] * maxn[0])