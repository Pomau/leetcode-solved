class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        alf = defaultdict(int)
        for el in arr:
            alf[el] += 1
        for key, item in alf.items():
            if item > len(arr) // 4:
                return key