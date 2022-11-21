class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remains = dict()
        sums = 0
        remains[0] = -1
        for i in range(len(nums)):
            sums += nums[i]
            if sums%k in remains and i - remains[sums%k] > 1:
                return True
            if sums%k not in remains:
                remains[sums%k] = i
        return False
        