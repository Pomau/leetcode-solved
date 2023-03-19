class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = 0
        ans = []
        for i, ch in enumerate(arr):
            if ch == 0:
                ans.append(0)
            ans.append(ch)
        for i in range(len(arr)):
            arr[i] = ans[i]