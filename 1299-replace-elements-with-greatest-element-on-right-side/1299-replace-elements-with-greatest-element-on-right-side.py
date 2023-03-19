class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix = [-1]
        for i in range(len(arr) - 1, 0, -1):
            suffix.append(max(arr[i], suffix[-1]))
        suffix.reverse()
        return suffix
        