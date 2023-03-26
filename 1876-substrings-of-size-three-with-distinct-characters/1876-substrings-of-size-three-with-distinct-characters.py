class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        alf = defaultdict(int)
        ans = 0
        for i, el in enumerate(s):
            alf[el] += 1
            if i >= 3:
                alf[s[i - 3]] -= 1
                if alf[s[i-3]] == 0:
                    del alf[s[i-3]]
            if len(alf) == 3:
                ans += 1
        return ans