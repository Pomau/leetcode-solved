class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.brute(set(nums), [])
        return self.result
    def brute(self, alf, ans):
        if len(alf) == 0:
            self.result.append(ans)
            return
        for ch in list(alf):
            alf.remove(ch)
            self.brute(alf, ans+ [ch])
            alf.add(ch)