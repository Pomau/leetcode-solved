class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alf = defaultdict(int)
        for ch in s1:
            alf[ch] += 1
        for r in range(len(s2)):
            alf[s2[r]] -= 1
            if alf[s2[r]] == 0:
                del alf[s2[r]]
            if r >= len(s1):
                alf[s2[r - len(s1)]] += 1
                if alf[s2[r - len(s1)]] == 0:
                    del alf[s2[r - len(s1)]]
            if len(alf) == 0:
                return True
        return False
            