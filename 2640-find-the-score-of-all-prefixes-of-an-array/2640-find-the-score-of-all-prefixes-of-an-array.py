class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefix = []
        maxn = 0
        for i in range(len(nums)):
            maxn = max(maxn, nums[i])
            prefix.append(nums[i] + maxn)
        ans = []
        sums = 0
        for i in range(len(nums)):
            sums += prefix[i]
            ans.append(sums)
        return ans