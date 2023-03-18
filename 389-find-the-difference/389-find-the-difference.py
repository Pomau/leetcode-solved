class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alf = defaultdict(int)
        for el in s:
            alf[el] += 1
        for el in t:
            alf[el] -= 1
            if alf[el] == -1:
                return el
        return -1
