class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alf = defaultdict(int)
        for i in s1:
            alf[i] += 1
        for i in range(len(s2)):
            alf[s2[i]] -= 1
            if alf[s2[i]] == 0:
                del alf[s2[i]]
            if i >= len(s1):
                alf[s2[i - len(s1)]] += 1
                if alf[s2[i - len(s1)]] == 0:
                    del alf[s2[i - len(s1)]]
            if len(alf) == 0:
                return True
        return False
