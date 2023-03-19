class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        alf = defaultdict(int)
        for i in arr1:
            alf[i] += 1
        ans = []
        for i in arr2:
            while alf[i] > 0:
                alf[i] -= 1
                ans.append(i)
            del alf[i]
        arr = []
        for key, item in alf.items():
            while item > 0:
                arr.append(key)
                item -= 1
        arr.sort()
        return ans + arr