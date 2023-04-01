class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ind = [[nums[i], i] for i in range(len(nums))]
        ind.sort()
        ans_ind = [[ind[i][1], ind[i][0]] for i in range(len(ind) - k, len(ind))]
        ans_ind.sort()
        return [ans[1] for ans in ans_ind]