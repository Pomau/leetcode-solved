import random
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = -1
        while nums.count(k) != 0:
            k = random.randint(-2**31, -1)
        for i in range(len(nums)):
            while nums[i] > 0:
                number = nums[i] - 1
                if 0 <= number < len(nums) and nums[number] != k:
                    nums[i] = nums[number]
                    nums[number] = k
                else:
                    break
        answer = 0
        while answer < len(nums) and nums[answer] == k:
            answer += 1
        return answer + 1
# -5 1 k =-5
        