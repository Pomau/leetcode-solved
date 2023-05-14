class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.used = [False] * len(nums)
        self.used_num = set()
        self.nums = nums
        self.ans = 0
        self.hashes = defaultdict(int)
        self.gcd_h = dict()
        

        return self.brute(0, len(nums), 1, 0)
    
    def brute(self, k, n, it, mask):
        if n == 0:
            self.ans = max(self.ans, k)
            return 0
        if mask in self.hashes:
            return self.hashes[mask]
        res = 0
        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            self.used[i] = True
            for j in range(i + 1, len(self.nums)):
                if self.used[j]:
                    continue
                self.used[j] = True
                new_m =  mask | (1 << i) | (1 << j)
                new = it * self.gcd(self.nums[i], self.nums[j])
                res1 = self.brute(new + k, n - 2, it + 1, new_m)
                res = max(res1 + new, res)
                self.used[j] = False
            self.used[i] = False
        self.hashes[mask] = res
        return res 
    def gcd(self, a, b):
        tup = tuple(sorted([a, b]))
        if tup in self.gcd_h:
            return self.gcd_h[tup]
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        self.gcd_h[tup] = a + b
        return a + b
                