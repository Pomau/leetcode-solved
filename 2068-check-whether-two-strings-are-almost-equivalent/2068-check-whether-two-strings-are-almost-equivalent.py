class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        alf = defaultdict(int)
        for ch in word1:
            alf[ch] += 1
        for ch in word2:
            alf[ch] -= 1
        for key, item in alf.items():
            if abs(item) > 3:
                return False
        return True