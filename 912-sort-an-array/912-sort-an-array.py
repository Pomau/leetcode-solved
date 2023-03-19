class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(nums)
        for i in range(n -1 , -1, -1):
            self.push_vniz(i, n)
        for i in range(n):
            self.nums[0], self.nums[n - i - 1] = self.nums[n - i - 1], self.nums[0]
            self.push_vniz(0, n - i - 1)
        return self.nums
    def push_vniz(self, i, n):
        now = i
        while True:
            l = now * 2 + 1
            r = now * 2 + 2
            max_n = now
            if l < n and self.nums[max_n] < self.nums[l]:
                max_n = l
            if r < n and self.nums[max_n] < self.nums[r]:
                max_n = r
            if max_n == now:
                break
            self.nums[max_n], self.nums[now] = self.nums[now], self.nums[max_n]
            now = max_n