class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        alf = defaultdict(int)
        for ch in s:
            alf[ch] += 1
        k = None
        for key, item in alf.items():
            if k == None:
                k = item
            if k != item:
                return False
        return True