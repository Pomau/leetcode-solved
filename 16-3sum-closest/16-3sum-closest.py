class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float("inf")
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                sums = nums[i] + nums[l] + nums[r]
                if sums > target:
                    r -= 1
                else:
                    l += 1
                if abs(target - answer) > abs(target - sums):
                    answer = sums
        return answer
                