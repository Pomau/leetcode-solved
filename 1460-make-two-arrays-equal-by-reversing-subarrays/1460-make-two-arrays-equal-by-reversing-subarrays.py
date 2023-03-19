class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(len(arr)):
            if target[i] not in arr[i:]:
                return False
            ind = arr.index(target[i], i)
            arr = arr[:i] + arr[i:ind + 1][::-1] + arr[ind + 1:]
        return arr == target