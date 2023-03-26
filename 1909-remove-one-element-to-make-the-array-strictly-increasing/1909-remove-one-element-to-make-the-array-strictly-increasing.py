class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        k = [0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                k = [i, i - 1]
                break
        ans = False
        for j in k:
            os = True
            num = nums[:j] + nums[j + 1:]
            for i in range(1, len(num)):
                if num[i] <= num[i - 1]:
                    os = False
            ans = ans or os
        return ans