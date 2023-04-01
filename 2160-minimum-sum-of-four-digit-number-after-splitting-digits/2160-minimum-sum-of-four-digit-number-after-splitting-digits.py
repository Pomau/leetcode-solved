class Solution:
    def minimumSum(self, num: int) -> int:
        self.nums = defaultdict(int)
        num1 = num
        while num > 0:
            self.nums[num % 10] += 1
            num //= 10
        self.ans = float("inf")
        self.brute(0, 0, 0)
        if self.ans == float("inf"):
            return num1
        return self.ans
    def brute(self,l,  k1, k2):
        if l == 4:
            self.ans = min(self.ans, abs(k1 + k2))
            return
        for key, val in self.nums.items():
            if val > 0:
                self.nums[key] -= 1
                self.brute(l + 1, k1 * 10 + key, k2)
                self.brute(l + 1, k1, k2 * 10 + key)
                self.nums[key] += 1