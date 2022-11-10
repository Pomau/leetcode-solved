class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_collect = defaultdict(int)
        for ch in s1:
            s1_collect[ch] += 1
        s2_collect = defaultdict(int)
        for r in range(len(s2)):
            s2_collect[s2[r]] += 1
            if r >= len(s1):
                s2_collect[s2[r - len(s1)]] -= 1
                if s2_collect[s2[r - len(s1)]] == 0:
                    del s2_collect[s2[r - len(s1)]]
            if s1_collect == s2_collect:
                return True
        return False