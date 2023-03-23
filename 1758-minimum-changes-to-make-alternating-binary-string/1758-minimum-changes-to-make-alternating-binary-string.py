class Solution:
    def minOperations(self, s: str) -> int:
        nums = [int(s[i]) for i in range(len(s))]
        return min(self.solve(nums, 0), self.solve(nums, 1))
    
    def solve(self, nums, hod):
        ans = 0
        for i in range(len(nums)):
            if nums[i] != hod:
                ans += 1
            hod = 1 - hod
        return ans