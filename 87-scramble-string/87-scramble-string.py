class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        self.hash = {}
        self.s2 = s2
        self.s1 = s1
        return self.brute(0, len(s2), 0, len(s1))
    def brute(self, l, r, sl, sr):
        if r - l == 1:
            return self.s1[sl] == self.s2[l]
        tupl = (l, r, sl, sr)
        if tupl in self.hash:
            return self.hash[tupl]
        ans = False
        for k in range(1, r - l):
            prot = (r - l) - k
            if (self.brute(l, l + k, sl, sl + k) and self.brute(l + k, r, sl + k, sr) or 
                self.brute(l, l + prot, sl + k, sr) and self.brute(l + prot, r, sl, sl + k)):
                ans = True
        self.hash[tupl] = ans
        return ans