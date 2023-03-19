class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        ans = 0
        nums.sort(reverse= True)
        stack = []
        l = 0
        for i in range(len(nums)):
            if len(stack) > l and stack[l] > nums[i]:
                l += 1
                ans += 1
            stack.append(nums[i])
        return ans