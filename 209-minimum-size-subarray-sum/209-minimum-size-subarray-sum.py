class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = sums = 0
        answer = len(nums) + 1
        for r in range(len(nums)):
            sums += nums[r]
            while sums >= target and sums - nums[l] >= target:
                answer = min(answer, r - l + 1)
                sums -= nums[l]
                l += 1
            if sums >= target:
                answer = min(answer, r - l + 1)
        if answer == len(nums) + 1:
            answer = 0
        return answer
            
                
            