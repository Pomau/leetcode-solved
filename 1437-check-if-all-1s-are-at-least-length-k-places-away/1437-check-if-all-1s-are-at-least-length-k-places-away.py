class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        alf = [0, 0]
        for i, num in enumerate(nums):
            alf[num] += 1
            if i >= k + 1:
                alf[nums[i - k - 1]] -= 1
            if alf[1] > 1:
                return False
        return True