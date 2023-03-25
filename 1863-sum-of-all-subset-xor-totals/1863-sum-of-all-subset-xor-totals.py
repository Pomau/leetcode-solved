class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        self.nums = nums
        for i in range(len(nums)):
            self.brute(i, 0)
        return self.ans
    def brute(self, i, now):
        now ^= self.nums[i]
        self.ans += now
        for j in range(i + 1, len(self.nums)):
            self.brute(j, now)