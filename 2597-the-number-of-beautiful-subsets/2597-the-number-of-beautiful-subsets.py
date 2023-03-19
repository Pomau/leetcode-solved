class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0
        self.nums = sorted(nums)
        self.have = [False] * len(nums)
        self.l = 0
        self.k = k
        self.perebor(defaultdict(int))
        return self.ans
    def perebor(self, alf):
        if len(alf) > 0:
            self.ans += 1
        if self.l == len(self.nums):
            return
        now = self.l
        for i in range(self.l, len(self.nums)):
            now = self.nums[i]
            if now - self.k in alf:
                continue
            self.l = i + 1
            self.have[i] = True
            alf[now] += 1
            self.perebor(alf)
            alf[now] -= 1
            self.have[i] = False
            if alf[now] == 0:
                del alf[now]
        self.l = now