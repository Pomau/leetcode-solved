class Solution:
    def minInsertions(self, s: str) -> int:
        self.alf = {}
        self.s = s
        n = self.brute(0, len(s) - 1)
        # print(self.alf)
        return len(s) - n
    
    def brute(self, l, r):
        if l > r:
            return 0
        if r == l:
            return 1
        pair = (l, r)
        if pair in self.alf:
            return self.alf[pair]
        if self.s[l] == self.s[r]:
            self.alf[pair] = self.brute(l + 1, r - 1) + 2
        else:
            self.alf[pair] = max(self.brute(l + 1, r), self.brute(l, r - 1))
        return self.alf[pair]
        