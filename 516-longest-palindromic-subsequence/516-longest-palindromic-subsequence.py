from bisect import bisect_left, bisect_right

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        self.map = {}
        self.alf = defaultdict(list)
        return self.brute(0, len(s) - 1)
    
    def brute(self, l, r):
        if (l, r) in self.map:
            #  print(l, r)
            return self.map[(l, r)]
        if r < l:
            return 0
        if r == l:
            return 1
        if self.s[l] == self.s[r]:
            self.map[(l, r)] = self.brute(l + 1, r - 1) + 2
        else:
            self.map[(l, r)] = max(self.brute(l, r - 1), self.brute(l + 1, r))
        return self.map[(l, r)]