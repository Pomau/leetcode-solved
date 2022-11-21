class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        tranformer_count = 0
        answer = 0
        for r in range(len(nums)):
            tranformer_count += (nums[r] == 0)
            while tranformer_count > k:
                tranformer_count -= (nums[l] == 0)
                l += 1
            answer = max(answer, r - l + 1)
        return answer                