class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr = []
        for r, num in enumerate(nums):
            arr.append([num, r])
            arr.sort(reverse=True)
            if len(arr) > 2:
                arr.pop()
        if (arr[0][0] >= arr[1][0] * 2):
            return arr[0][1]
        return -1