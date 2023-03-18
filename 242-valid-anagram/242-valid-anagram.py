class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alf = defaultdict(int)
        for ch in s:
            alf[ch] += 1
        for ch in t:
            alf[ch] -= 1
            if alf[ch] == 0:
                del alf[ch]
        return len(alf) == 0