class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        count_k = 0
        answer = 0
        for r in range(len(nums)):
            count_k += (nums[r] == 0)
            while count_k > 1:
                count_k -=  (nums[l] == 0)
                l += 1
            answer = max(answer, r - l)
        return answer